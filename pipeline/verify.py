"""
Verify URL liveness for all sources in data/sources.csv.

For each source URL:
  1. HEAD request (fast, most servers OK)
  2. Fallback GET with stream=False if HEAD → 405 / 0
  3. If dead → probe Wayback Machine for archived copy
  4. Stamps status + retrieved_at in sources.csv

Outputs a human-readable report showing what changed.

Usage:
    python -m pipeline.verify                      # dry-run, print report
    python -m pipeline.verify --apply              # update data/sources.csv
    python -m pipeline.verify --older-than 90      # only re-check stale sources
    python -m pipeline.verify --id nsd             # check sources for one entity

The script depends only on Python 3.8+ stdlib (urllib, http.client).
No requests / httpx required — matches healthaiatlas zero-dependency style.
"""
from __future__ import annotations

import argparse
import csv
import http.client
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime
from pathlib import Path

# Force UTF-8 on Windows consoles that default to cp1252
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace", line_buffering=True)
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8",
                                  errors="replace", line_buffering=True)

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

DATA_DIR = ROOT / "data"
TODAY = date.today().isoformat()

TIMEOUT = 10          # seconds per HTTP attempt

# Hosts where redirect means "URL has permanently moved" → auto-update url field
# DOI URLs are intentionally indirect (doi.org → publisher) → never auto-update
AUTO_FOLLOW_REDIRECT_HOSTS = frozenset({
    "openneuro.org",
    "github.com",
    "zenodo.org",
    "figshare.com",
    "osf.io",
    "nitrc.org",
    "crcns.org",
})
HEAD_SLEEP = 0.3      # polite delay between requests
WAYBACK_SLEEP = 1.5   # Wayback is slower — be polite

# Confidence tiers by domain pattern (mirrors healthaiatlas predicates.py)
DOMAIN_TIERS = {
    "doi.org":           "high",
    "nature.com":        "high",
    "science.org":       "high",
    "nih.gov":           "high",
    "openneuro.org":     "high",
    "zenodo.org":        "high",
    "pmc.ncbi.nlm.nih.gov": "high",
    "elifesciences.org": "high",
    "biorxiv.org":       "medium",
    "medrxiv.org":       "medium",
    "arxiv.org":         "medium",
    "github.com":        "medium",
    "figshare.com":      "medium",
}

_UA = "brain-encoder-datasets/verify.py (academic catalog; contact: kondratevakate@gmail.com)"


def _should_auto_follow_redirect(url: str, code: int) -> bool:
    """
    True if a redirect for this URL should automatically update sources.csv.

    Rules:
    - doi.org is intentionally indirect — never follow (would replace
      stable DOI with fragile publisher URL)
    - Permanent redirects (308) on known stable hosts → auto-follow
    - Temporary redirects (302) → never auto-follow (may be transient)
    - 301 on known hosts → auto-follow (they don't use 308 consistently)
    """
    parsed = urllib.parse.urlparse(url)
    host = parsed.netloc.lstrip("www.")
    if "doi.org" in host:
        return False
    if code == 308:
        return True
    if code == 301:
        return any(host.endswith(h) for h in AUTO_FOLLOW_REDIRECT_HOSTS)
    return False


def _domain_tier(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    host = parsed.netloc.lstrip("www.")
    for pattern, tier in DOMAIN_TIERS.items():
        if host.endswith(pattern):
            return tier
    return "medium"


def _head(url: str) -> tuple[int, str]:
    """Return (status_code, redirect_url_or_empty). Raises on timeout."""
    req = urllib.request.Request(url, method="HEAD",
                                 headers={"User-Agent": _UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.status, resp.url if resp.url != url else ""
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return 0, str(e)


def _get_shallow(url: str) -> int:
    """GET with immediate close — for servers that reject HEAD."""
    req = urllib.request.Request(url, headers={"User-Agent": _UA,
                                               "Range": "bytes=0-0"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return 0


def _wayback_probe(url: str) -> str:
    """
    Probe Wayback Machine for an archived copy.
    Uses the /web/0/ redirect trick (no rate-limit, unlike /available API).
    Returns the archived URL string, or '' if not found.
    """
    wayback_url = f"https://web.archive.org/web/0/{url}"
    req = urllib.request.Request(wayback_url, method="HEAD",
                                 headers={"User-Agent": _UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            # Wayback redirects to the nearest snapshot
            final = resp.url
            if "web.archive.org/web/" in final and final != wayback_url:
                return final
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return ""
        # Other errors → treat as not found
    except Exception:
        pass
    return ""


def check_url(url: str) -> dict:
    """
    Full liveness check for one URL.
    Returns dict with keys: status, redirect_url, wayback_url, tier.
    """
    if not url or not url.startswith("http"):
        return {"status": "skip", "redirect_url": "", "wayback_url": "", "tier": "low"}

    code, redirect = _head(url)
    time.sleep(HEAD_SLEEP)

    if code in (301, 302, 303, 307, 308) and redirect:
        return {"status": "redirect", "redirect_url": redirect,
                "wayback_url": "", "tier": _domain_tier(url)}

    if code == 405:
        # Server rejected HEAD — retry with GET
        code = _get_shallow(url)
        time.sleep(HEAD_SLEEP)

    if 200 <= code < 400:
        return {"status": "ok", "redirect_url": "",
                "wayback_url": "", "tier": _domain_tier(url)}

    # Dead or unreachable — probe Wayback
    time.sleep(WAYBACK_SLEEP)
    wayback = _wayback_probe(url)
    status = "dead_archived" if wayback else "dead"
    return {"status": status, "redirect_url": "", "wayback_url": wayback,
            "tier": _domain_tier(url)}


def load_sources() -> list[dict]:
    path = DATA_DIR / "sources.csv"
    if not path.exists():
        print(f"ERROR: {path} not found — run pipeline/migrate.py --apply first",
              file=sys.stderr)
        sys.exit(1)
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_claims() -> list[dict]:
    path = DATA_DIR / "claims.csv"
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _entity_ids_for_source(source_id: str, claims: list[dict]) -> list[str]:
    return list({c["entity_id"] for c in claims
                 if source_id in c.get("source_ids", "").split(";")})


def _is_stale(source: dict, older_than_days: int) -> bool:
    retrieved = source.get("retrieved_at", "")
    if not retrieved:
        return True
    try:
        dt = datetime.fromisoformat(retrieved)
        age = (datetime.now() - dt).days
        return age >= older_than_days
    except ValueError:
        return True


def verify(
    apply: bool,
    older_than_days: int | None,
    entity_filter: str | None,
) -> None:
    sources = load_sources()
    claims  = load_claims()

    # Build filter set of source_ids relevant to entity_filter
    if entity_filter:
        relevant_sids = {
            sid.strip()
            for c in claims if c["entity_id"] == entity_filter
            for sid in c.get("source_ids", "").split(";")
            if sid.strip()
        }
        sources = [s for s in sources if s["source_id"] in relevant_sids]
        if not sources:
            print(f"No sources found for entity {entity_filter!r}")
            return

    # Staleness filter
    if older_than_days is not None:
        to_check = [s for s in sources if _is_stale(s, older_than_days)]
    else:
        to_check = sources

    print(f"Checking {len(to_check)} source(s) "
          f"({'all' if older_than_days is None else f'stale >{older_than_days}d'})...\n")

    results: list[tuple[dict, dict]] = []   # (original_source, check_result)
    for i, source in enumerate(to_check, 1):
        url = source["url"]
        print(f"  [{i}/{len(to_check)}] {url[:72]}...", end=" ", flush=True)
        result = check_url(url)
        print(result["status"])
        results.append((source, result))

    # --- Report ---
    changed: list[dict] = []
    summary = {"ok": 0, "redirect": 0, "dead": 0, "dead_archived": 0,
               "skip": 0, "unchanged": 0}

    print("\n--- Results ---")
    for source, result in results:
        old_status = source.get("status", "unverified")
        new_status = result["status"]
        summary[new_status] = summary.get(new_status, 0) + 1

        if new_status != old_status or result.get("wayback_url"):
            entity_ids = _entity_ids_for_source(source["source_id"], claims)
            tag = f"[{', '.join(entity_ids)}]" if entity_ids else ""
            print(f"  {old_status} -> {new_status}  {source['url'][:60]}  {tag}")
            redirect_url = result.get("redirect_url", "")
            if redirect_url:
                auto = _should_auto_follow_redirect(source["url"], 301)
                action = "auto-updating url" if auto else "flagged for manual review"
                print(f"    redirect -> {redirect_url}  ({action})")
            if result.get("wayback_url"):
                print(f"    wayback  -> {result['wayback_url']}")

            # Build updated source record
            updated = {**source,
                       "status": new_status,
                       "retrieved_at": TODAY,
                       "wayback_url": result.get("wayback_url",
                                                  source.get("wayback_url", ""))}
            # Auto-follow redirect only for approved hosts, never for DOI
            if redirect_url and _should_auto_follow_redirect(source["url"], 301):
                updated["url"] = redirect_url
                updated["status"] = "ok"   # now points directly to live target
            changed.append(updated)
        else:
            summary["unchanged"] = summary.get("unchanged", 0) + 1

    print(f"\nSummary: {summary}")
    print(f"Changed: {len(changed)}")

    if not changed:
        print("Nothing to update.")
        return

    if not apply:
        print("\nDry-run. Re-run with --apply to update data/sources.csv.")
        return

    # --- Apply: merge changes back into sources list ---
    changed_by_id = {s["source_id"]: s for s in changed}
    updated_sources = [changed_by_id.get(s["source_id"], s) for s in sources]

    from schema.schema import SOURCE_COLUMNS
    with (DATA_DIR / "sources.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=SOURCE_COLUMNS)
        w.writeheader()
        for s in updated_sources:
            w.writerow({k: s.get(k, "") for k in SOURCE_COLUMNS})

    print(f"Updated data/sources.csv ({len(changed)} record(s) changed).")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true",
                        help="Write changes to data/sources.csv")
    parser.add_argument("--older-than", type=int, metavar="DAYS",
                        dest="older_than",
                        help="Only re-check sources not verified in N days")
    parser.add_argument("--id", metavar="ENTITY_ID",
                        dest="entity_id",
                        help="Only check sources for this entity (e.g. 'nsd')")
    args = parser.parse_args()
    verify(apply=args.apply,
           older_than_days=args.older_than,
           entity_filter=args.entity_id)


if __name__ == "__main__":
    main()
