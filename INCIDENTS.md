# Incidents log — production fuckups → hard rules

Format inspired by `healthaiatlas/AGENTS.md` "Hard rules — production incidents log". These are not abstract guidelines. Each entry documents a real failure caught during automated verification, and the rule it produced. Future agents and humans contributing to this catalog must follow them.

---

## Incident 1: Hallucinated and mis-assigned DOIs in `datasets.bib`

**Date:** 2026-05-31
**Severity:** High — academic citations are not recoverable once shared. A wrong DOI in a reference list is one of the most visible signs of AI-generated content and gets papers desk-rejected.
**Audit trail:** [`verification/2026-05-31_initial_audit.md`](verification/2026-05-31_initial_audit.md)

**What happened:** The initial `datasets.bib` was hand-written by Claude from memory and search-result snippets, then committed without verification. Running [`bib-verify`](https://github.com/anthropics/skills) against Crossref revealed:

- **32 entries audited** → 22 verified ✓ / **6 hallucination** / **2 placeholder** / **1 substitution** / **1 mismatch**.
- **Hallucination rate: 28%** (9 out of 32 problematic).

Concrete failures:

| Entry key | Failure mode | What was wrong | What it actually is |
|---|---|---|---|
| `barch2013hcptask` | wrong DOI | claimed `10.1016/j.neuroimage.2013.05.041` | correct is `10.1016/j.neuroimage.2013.05.033` — the wrong DOI points to "WU-Minn HCP Overview" by Van Essen et al. |
| `casey2018abcd` | wrong DOI | claimed `10.1016/j.dcn.2018.04.004` | correct is `10.1016/j.dcn.2018.03.001` — the wrong DOI points to "Recruiting the ABCD sample" by Garavan et al. |
| `kessler2021adhd` | catastrophic DOI mismatch | DOI `10.1038/s41597-021-00921-y` actually points to **"IDEAL household energy dataset for 255 UK homes"** — a paper about home energy consumption, unrelated to neuroimaging | correct paper is Lytle, Burman & Booth, *Data in Brief* 2021, DOI `10.1016/j.dib.2021.107158`. Entry key renamed to `lytle2021adhd`. The author "Kessler, Daniel" was fabricated. |
| `liberto2025cospine` | fabricated first author | author "Liberto" was invented; DOI correctly resolved to "CoSpine open access fMRI database" but the real first author is **Wei, Zhaoxing**. Entry key renamed to `wei2025cospine`. |
| `nfed2024` | `{Anonymous}` author placeholder | wrote `author = {{Anonymous}}` instead of looking up the real authors | real first author is **Chen, Panpan** plus 8 co-authors. Entry key renamed to `chen2024nfed`. |
| `lespinasse2025cneuromodthings` | year mismatch + "and others" after 1 author | claimed year 2025; Crossref says 2026. Author list was `{Lespinasse, François and others}` with only one named author. | corrected to 2026; entry key renamed to `lespinasse2026cneuromodthings`; flagged with `note` that full author list still needs verification |
| `lahner2024bmd` | "and others" hiding 10 missing co-authors | wrote `{Lahner, B. and Mohsenzadeh, Y. and Mongiat, C. and others}` — only 3 of 13 named, and 2 of those 3 (Mohsenzadeh, Mongiat) **are not on the paper** | corrected to actual 13-author list per Crossref |
| `gifford2025algonauts` | placeholder citation | `journal = {arXiv preprint}, volume = {2501.00504}` — wrong entry type, author "Gifford, Alessandro T. and others" with only 1 named author | converted to `@misc` with proper `eprint` / `archivePrefix`; note added that author list is partial pending arXiv verification |
| `benchetrit2025tribe` | wrong first author + placeholder citation | claimed `author = {{Meta FAIR}}` as institutional author; real first author is **d'Ascoli, Stéphane**. arXiv ID was correct (2507.22229) but in the wrong field | entry key renamed to `dascoli2025tribe`; full 5-author list added |

### Rule 1.1 — Never write a BibTeX entry from memory

**Procedure for adding any BibTeX entry:**

1. Get the canonical reference from one of: Crossref API, arXiv API, PubMed, the paper's own landing page.
2. Copy the metadata as-is. Do not modify author names, year, or DOI based on assumptions.
3. If the entry comes from a press release, blog, or news article, that is **not sufficient sourcing** — find the underlying paper before committing.
4. If full author list is unwieldy, list at least the first 3 authors before `et al.` / `and others`. Never use `and others` after a single named author.
5. If the author is genuinely unknown or institutional, use `{{Institution Name}}` with double braces, not `{Anonymous}`.

### Rule 1.2 — Verify every BibTeX file before commit

Run [`bib-verify`](https://github.com/anthropics/skills) (or equivalent Crossref check) on the `.bib` file before any commit that adds or modifies entries. Save the audit report to `verification/<YYYY-MM-DD>_<description>.md` for the audit trail.

Pre-commit hook is preferred. CI gate is mandatory before publication of any artifact that consumes `datasets.bib`.

### Rule 1.3 — Wrong DOI is worse than missing DOI

If you cannot verify the DOI against Crossref, leave the `doi` field empty. An entry with no DOI is honest. An entry with a DOI pointing to the wrong paper is a citation crime — the reader is sent to a completely unrelated work and assumes the catalog author was confused or dishonest. The `kessler2021adhd → IDEAL household energy dataset` case is the canonical example.

### Rule 1.4 — Author lists are facts, not stubs

`author = {Liberto, ...}` where "Liberto" was guessed from the dataset name "CoSpine" caused a real fabricated author. The procedure:

- Always fetch the author list from the resolved Crossref/arXiv record.
- Do not infer an author from a project name, lab name, or institution.
- If the entry key includes an author name, that name must match the actual first author. If the project name changes lead author, rename the entry key.

---

## Summary — pre-commit checklist for any change touching `datasets.bib`

- [ ] Every `doi` field has been live-resolved against Crossref and points to the correct paper.
- [ ] Every `author` field lists at least 3 real authors before `and others`, copied from the resolved record.
- [ ] No `{{Anonymous}}` or single-author-with-`and others` patterns.
- [ ] Entry type matches the venue (`@article` for journals, `@misc` for arXiv preprints, `@inproceedings` for actual conference proceedings).
- [ ] `bib-verify` report shows zero hallucination / placeholder verdicts.
- [ ] Audit report saved to `verification/`.
- [ ] If you fixed entries based on an audit, link the audit report in the commit message.

---

## Why this file exists

The first round of the catalog had a 28% hallucination rate in citations. The cost of fixing it after publication would be much higher than the cost of preventing it. This log exists so the next agent (or human) knows the failure modes by example, not by abstract principle.

Inspired by [`healthaiatlas/AGENTS.md`](https://github.com/kondratevakate/healthaiatlas) production-incidents-log format.
