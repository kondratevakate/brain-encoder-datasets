"""
Regenerate derived artifacts from the three-table schema.

Produces:
  - datasets.csv       (flat view, backwards-compatible legacy format)
  - POPULATION_MATRIX.md  (auto-generated, do not edit manually)

Does NOT touch:
  - Human-written README sections (everything outside AUTO-GENERATED blocks)
  - datasets.bib (maintained separately)

Usage:
    python -m pipeline.publish               # dry-run (shows what would change)
    python -m pipeline.publish --apply       # write files
"""
from __future__ import annotations

import argparse
import csv
import io
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from schema.predicates import ALL_PREDICATES

DATA_DIR = ROOT / "data"

# Sentinel strings that mark the auto-generated blocks in markdown files.
# Everything between BEGIN and END is replaced by publish.py.
# Do not modify these strings — they're load-bearing.
MATRIX_BEGIN = "<!-- BEGIN AUTO-GENERATED POPULATION_MATRIX -->"
MATRIX_END   = "<!-- END AUTO-GENERATED POPULATION_MATRIX -->"

STIMULUS_ORDER = [
    "image", "video", "film", "tv", "music", "speech",
    "decision", "pain", "motor", "interactive", "mixed",
]

POPULATION_ORDER = [
    "healthy-adult", "healthy-aging", "pediatric",
    "pediatric-clinical", "asd", "adhd",
    "scz", "mdd", "ptsd",
    "stroke", "ad", "mci", "pain", "addiction", "mixed-clinical",
]


def load_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build_entity_claims(entities: list[dict], claims: list[dict]) -> dict[str, dict]:
    """Build {entity_id: {predicate: value}} lookup."""
    ec: dict[str, dict] = {e["entity_id"]: {"entity_id": e["entity_id"],
                                              "name": e["name"],
                                              "url": e["url"]}
                            for e in entities}
    for c in claims:
        eid = c["entity_id"]
        if eid in ec:
            ec[eid][c["predicate"]] = c["value"]
    return ec


def generate_flat_csv(entity_claims: dict[str, dict]) -> str:
    """Generate backwards-compatible flat datasets.csv content."""
    flat_columns = ["id", "name"] + ALL_PREDICATES
    rows = []
    for eid, ec in entity_claims.items():
        row = {"id": eid, "name": ec.get("name", "")}
        for pred in ALL_PREDICATES:
            row[pred] = ec.get(pred, "")
        # url is stored in entity row, map it to the url predicate slot
        if not row.get("url"):
            row["url"] = ec.get("url", "")
        rows.append(row)
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=flat_columns,
                            extrasaction="ignore", quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
    return buf.getvalue()


def generate_matrix(entity_claims: dict[str, dict]) -> str:
    """Generate POPULATION_MATRIX markdown table from claims."""
    # Build population × stimulus_modality → [entity_ids]
    grid: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    for eid, ec in entity_claims.items():
        pop = ec.get("population", "")
        mod = ec.get("stimulus_modality", "")
        if pop and mod:
            grid[pop][mod].append(eid)

    populations = [p for p in POPULATION_ORDER if p in grid] + \
                  [p for p in grid if p not in POPULATION_ORDER]
    stimuli = [s for s in STIMULUS_ORDER if any(s in grid[p] for p in populations)] + \
              [s for s in set(m for p in grid.values() for m in p) if s not in STIMULUS_ORDER]

    header = "| Population ↓ / Stimulus → | " + " | ".join(stimuli) + " |"
    sep    = "|---|" + "---|" * len(stimuli)
    lines  = [header, sep]

    for pop in populations:
        cells = []
        for mod in stimuli:
            ids = grid[pop].get(mod, [])
            cells.append(", ".join(ids) if ids else "—")
        lines.append(f"| **{pop}** | " + " | ".join(cells) + " |")

    return "\n".join(lines)


def publish(apply: bool) -> None:
    for name in ("entities.csv", "claims.csv"):
        if not (DATA_DIR / name).exists():
            print(f"ERROR: {DATA_DIR / name} not found — run pipeline/migrate.py --apply first",
                  file=sys.stderr)
            sys.exit(1)

    entities = load_csv(DATA_DIR / "entities.csv")
    claims   = load_csv(DATA_DIR / "claims.csv")
    ec = build_entity_claims(entities, claims)

    # --- flat datasets.csv ---
    flat_content = generate_flat_csv(ec)
    flat_path = ROOT / "datasets.csv"
    if apply:
        flat_path.write_text(flat_content, encoding="utf-8")
        print(f"Written: {flat_path} ({len(ec)} rows)")
    else:
        current = flat_path.read_text(encoding="utf-8") if flat_path.exists() else ""
        if current == flat_content:
            print("datasets.csv: no change")
        else:
            print(f"datasets.csv: would update ({len(ec)} entities)")

    # --- POPULATION_MATRIX.md ---
    matrix_md = generate_matrix(ec)
    matrix_path = ROOT / "POPULATION_MATRIX.md"

    if matrix_path.exists():
        current_matrix = matrix_path.read_text(encoding="utf-8")
        if MATRIX_BEGIN in current_matrix:
            before = current_matrix[:current_matrix.index(MATRIX_BEGIN) + len(MATRIX_BEGIN)]
            after_start = current_matrix.index(MATRIX_END)
            after = current_matrix[after_start:]
            new_matrix = before + "\n\n" + matrix_md + "\n\n" + after
        else:
            # Prepend auto-gen block to existing file
            new_matrix = (
                f"{MATRIX_BEGIN}\n\n{matrix_md}\n\n{MATRIX_END}\n\n"
                + current_matrix
            )
    else:
        new_matrix = (
            "# Population × Stimulus-Modality Coverage Matrix\n\n"
            "*Auto-generated by `pipeline/publish.py`. "
            "Edit the source data in `data/claims.csv`, not this file.*\n\n"
            f"{MATRIX_BEGIN}\n\n{matrix_md}\n\n{MATRIX_END}\n"
        )

    if apply:
        matrix_path.write_text(new_matrix, encoding="utf-8")
        print(f"Written: {matrix_path}")
    else:
        print(f"POPULATION_MATRIX.md: would update")
        print("\nMatrix preview:")
        for line in matrix_md.split("\n")[:5]:
            print(" ", line)
        print("  ...")

    if not apply:
        print("\nDry-run complete. Re-run with --apply to write files.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    publish(apply=args.apply)


if __name__ == "__main__":
    main()
