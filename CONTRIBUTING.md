# Contributing to brain-encoder-datasets

Pull requests welcome for new datasets, corrected links, updated access status, or new BibTeX entries.

> **Before you contribute:** read [`INCIDENTS.md`](INCIDENTS.md). It documents real failures (28% citation hallucination rate in the initial bib) and the hard rules that came out of them. Most importantly: **never write BibTeX from memory** — always live-resolve DOIs against Crossref.

## Adding a dataset

1. **Add a row to [`datasets.csv`](datasets.csv)** with all columns filled (use `-` if genuinely unknown — don't leave empty cells, they break CSV parsers). The row is the source of truth.
2. **Add a one-line entry to the matching section of [`README.md`](README.md)** with a markdown link to the landing page. Sort the section chronologically (newest first).
3. **Add a BibTeX entry to [`datasets.bib`](datasets.bib)** with the dataset's primary publication. Use the same `id` as the CSV row when sensible.
4. **Update [`POPULATION_MATRIX.md`](POPULATION_MATRIX.md)** if the new dataset fills a previously-empty cell (or adds substantially to an existing one).

## Criteria for inclusion

A dataset belongs here if **all three** of:

- It contains **fMRI** (not pure EEG/MEG/iEEG — those are valuable but out of scope; cross-modal datasets that include fMRI are fine).
- It has **stimulus-locked design** (events.tsv, stimulus onsets, or naturalistic timing) that could be used to train an encoder. Pure resting-state-only datasets don't fit — see [multiBrain](https://github.com/Conxz/multiBrain) for those.
- It's **accessible** in some form — open download, OpenNeuro, application-required, or institutional DUA. "I have it on a hard drive somewhere" doesn't count.

## What's out of scope

- Pure resting-state catalogs (→ multiBrain, CoRR)
- Pure structural / longitudinal aging without stimulus (→ multiBrain)
- Neuro-oncology image segmentation (→ TCIA collections, mentioned in multiBrain)
- Pre-registered datasets that aren't actually released yet

## Style

- Keep entries terse. README rows are one line. Long context goes in dedicated section text, not table rows.
- Use markdown links — never bare URLs in tables.
- Sort by year descending within each section.
- Date format: `YYYY` for `year` column, ISO `YYYY-MM-DD` only if a more precise release date matters.
- Cite the dataset paper, not your own work that uses it.

## Updating access status

Access changes (datasets going from "open" to "application", or vice versa). Run:

```bash
python scripts/check_openneuro_status.py
```

to refresh the `access` column for any OpenNeuro-hosted dataset.

## Questions

Open an issue. Friendly reviews; no obligation to be exhaustive in your first PR.
