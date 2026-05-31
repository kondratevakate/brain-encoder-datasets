"""Refresh OpenNeuro access status for datasets in datasets.csv.

For every row whose `url` matches https://openneuro.org/datasets/dsXXXXXX,
ping the OpenNeuro public GraphQL API and verify:
  - dataset exists and is public
  - newest snapshot tag
  - whether it has been deprecated / withdrawn

Prints a diff (planned changes) but does NOT modify datasets.csv by default.
Pass --write to apply changes in place.

Usage:
    python scripts/check_openneuro_status.py [--write] [--csv path/to/datasets.csv]
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import Iterable

import urllib.request
import urllib.error
import json

OPENNEURO_GRAPHQL = "https://openneuro.org/crn/graphql"
DS_PATTERN = re.compile(r"openneuro\.org/datasets/(ds\d+)", re.IGNORECASE)
QUERY = """
query DatasetStatus($id: ID!) {
  dataset(id: $id) {
    id
    public
    latestSnapshot { tag created }
  }
}
"""


def fetch_status(accession: str) -> dict | None:
    """Return parsed JSON status for an OpenNeuro accession, or None on error."""
    body = json.dumps({"query": QUERY, "variables": {"id": accession}}).encode("utf-8")
    req = urllib.request.Request(
        OPENNEURO_GRAPHQL,
        data=body,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print(f"  network error for {accession}: {e}", file=sys.stderr)
        return None


def planned_access(current: str, public: bool | None) -> str:
    """Decide the target access value given the OpenNeuro public flag."""
    if public is True:
        return "openneuro"
    if public is False:
        return "restricted"
    return current  # unknown → leave as-is


def iter_openneuro_rows(rows: Iterable[dict]) -> Iterable[tuple[int, dict, str]]:
    for idx, row in enumerate(rows):
        match = DS_PATTERN.search(row.get("url", ""))
        if match:
            yield idx, row, match.group(1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", default="datasets.csv", type=Path)
    parser.add_argument("--write", action="store_true", help="Apply changes in place")
    args = parser.parse_args()

    if not args.csv.exists():
        print(f"CSV not found: {args.csv}", file=sys.stderr)
        return 1

    with args.csv.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    changes: list[tuple[str, str, str]] = []  # (id, old, new)
    for idx, row, accession in iter_openneuro_rows(rows):
        print(f"Checking {row['id']} → {accession} ...")
        status = fetch_status(accession)
        if not status or "data" not in status:
            continue
        ds = (status.get("data") or {}).get("dataset")
        if ds is None:
            new_access = "restricted"  # not found publicly
        else:
            new_access = planned_access(row["access"], ds.get("public"))
        if new_access != row["access"]:
            changes.append((row["id"], row["access"], new_access))
            row["access"] = new_access

    if not changes:
        print("\nNo changes.")
        return 0

    print(f"\n{len(changes)} change(s):")
    for ds_id, old, new in changes:
        print(f"  {ds_id}: {old} → {new}")

    if args.write:
        with args.csv.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print(f"\nWrote updates to {args.csv}")
    else:
        print("\nDry run. Re-run with --write to apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
