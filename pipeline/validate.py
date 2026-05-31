"""
Enforce zero-trust invariants on the three-table schema.

Hard violations → exit 1 (CI gate).
Soft warnings  → print, exit 0.

Usage:
    python -m pipeline.validate             # check data/ directory
    python -m pipeline.validate --strict    # exit 1 on warnings too
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from schema.predicates import (
    ALL_PREDICATES, SOURCED_PREDICATES,
    STIMULUS_MODALITY_VALUES, POPULATION_VALUES, ACCESS_VALUES,
    BIDS_VALUES, CONFIDENCE_VALUES,
)

DATA_DIR = ROOT / "data"


def load_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def validate(strict: bool = False) -> bool:
    errors: list[str] = []
    warnings: list[str] = []

    # ---- Load tables ----
    for name in ("entities.csv", "claims.csv", "sources.csv"):
        if not (DATA_DIR / name).exists():
            errors.append(f"Missing file: data/{name} — run pipeline/migrate.py --apply first")
    if errors:
        _report(errors, warnings, strict)
        return False

    entities = load_csv(DATA_DIR / "entities.csv")
    claims   = load_csv(DATA_DIR / "claims.csv")
    sources  = load_csv(DATA_DIR / "sources.csv")

    entity_ids = {e["entity_id"] for e in entities}
    source_ids = {s["source_id"] for s in sources}
    claim_ids: set[str] = set()

    # ---- Entity invariants ----
    seen_entity_ids: set[str] = set()
    for e in entities:
        eid = e["entity_id"]
        if not eid:
            errors.append(f"Entity row with empty entity_id: {e}")
        if eid in seen_entity_ids:
            errors.append(f"Duplicate entity_id: {eid!r}")
        seen_entity_ids.add(eid)
        if not e.get("url"):
            warnings.append(f"Entity {eid!r}: missing url")

    # ---- Source invariants ----
    seen_source_urls: set[str] = set()
    for s in sources:
        url = s.get("url", "")
        if not url:
            errors.append(f"Source {s.get('source_id')!r} has empty url")
        if url in seen_source_urls:
            errors.append(f"Duplicate source url: {url!r}")
        seen_source_urls.add(url)

    # ---- Claim invariants ----
    for c in claims:
        cid = c.get("claim_id", "")
        eid = c.get("entity_id", "")
        predicate = c.get("predicate", "")
        value = c.get("value", "")
        src_ids_raw = c.get("source_ids", "")
        confidence = c.get("confidence", "")

        # Uniqueness
        if cid in claim_ids:
            errors.append(f"Duplicate claim_id: {cid!r}")
        claim_ids.add(cid)

        # FK: entity must exist
        if eid not in entity_ids:
            errors.append(f"Claim {cid!r}: entity_id {eid!r} not in entities.csv")

        # Predicate must be locked
        if predicate not in ALL_PREDICATES:
            errors.append(f"Claim {cid!r}: unknown predicate {predicate!r} (add to schema/predicates.py first)")

        # Confidence must be valid
        if confidence not in CONFIDENCE_VALUES:
            errors.append(f"Claim {cid!r}: invalid confidence {confidence!r}")

        # Source FK integrity
        if src_ids_raw:
            for sid in src_ids_raw.split(";"):
                sid = sid.strip()
                if sid and sid not in source_ids:
                    errors.append(f"Claim {cid!r}: source_id {sid!r} not in sources.csv")

        # Zero-trust: claims on SOURCED_PREDICATES must have a source
        if predicate in SOURCED_PREDICATES:
            if not src_ids_raw.strip():
                if confidence == "unverified":
                    warnings.append(f"Claim {cid!r} ({predicate}={value!r}): no source, marked unverified — needs manual verification")
                else:
                    errors.append(
                        f"Claim {cid!r} ({predicate}={value!r}): "
                        f"this predicate requires a source_id (see INCIDENTS.md #1). "
                        f"Set confidence='unverified' to acknowledge explicitly."
                    )

        # Enum validation
        if predicate == "stimulus_modality" and value not in STIMULUS_MODALITY_VALUES:
            errors.append(f"Claim {cid!r}: stimulus_modality value {value!r} not in locked enum")
        if predicate == "population" and value not in POPULATION_VALUES:
            errors.append(f"Claim {cid!r}: population value {value!r} not in locked enum")
        if predicate == "access" and value not in ACCESS_VALUES:
            errors.append(f"Claim {cid!r}: access value {value!r} not in locked enum")
        if predicate == "bids_compliant" and value not in BIDS_VALUES:
            errors.append(f"Claim {cid!r}: bids_compliant value {value!r} not in locked enum")

    # ---- Cross-table coverage ----
    # Every entity should have at least a url and access claim
    entity_predicates: dict[str, set[str]] = {e["entity_id"]: set() for e in entities}
    for c in claims:
        entity_predicates[c["entity_id"]].add(c["predicate"])

    for eid, predicates in entity_predicates.items():
        if "url" not in predicates:
            warnings.append(f"Entity {eid!r}: no url claim")
        if "access" not in predicates:
            warnings.append(f"Entity {eid!r}: no access claim (open/openneuro/application/restricted?)")

    # Orphan sources (no claim references them)
    claimed_source_ids: set[str] = set()
    for c in claims:
        for sid in c.get("source_ids", "").split(";"):
            if sid.strip():
                claimed_source_ids.add(sid.strip())
    for s in sources:
        if s["source_id"] not in claimed_source_ids:
            warnings.append(f"Orphan source {s['source_id']!r} ({s['url']!r}) — not referenced by any claim")

    return _report(errors, warnings, strict)


def _report(errors: list[str], warnings: list[str], strict: bool) -> bool:
    ok = True
    if warnings:
        print(f"\nWARN: {len(warnings)} warning(s):")
        for w in warnings:
            print(f"  - {w}")
    if errors:
        print(f"\nFAIL: {len(errors)} hard violation(s):")
        for e in errors:
            print(f"  - {e}")
        ok = False
    if strict and warnings:
        ok = False
    if ok and not warnings:
        print("OK: All invariants satisfied.")
    return ok


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true",
                        help="Exit 1 on warnings too (use in CI)")
    args = parser.parse_args()
    ok = validate(strict=args.strict)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
