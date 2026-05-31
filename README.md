# brain-encoder-datasets

A curated catalog of fMRI datasets useful for training and benchmarking **brain encoders / decoders** — models that map between rich stimuli (images, video, film, music, speech, decisions, pain) and BOLD responses. Inspired by [multiBrain](https://github.com/Conxz/multiBrain), but organized around **stimulus modality and population** instead of repeat-scan reliability.

If you're training something TRIBE-, MindEye-, or Tang-and-LeBel-like, this is the index to start from.

---

## Why this exists

Most public fMRI catalogs are organized around **clinical populations** (ADNI, OASIS, PPMI) or **scan-rescan reliability** (multiBrain, CoRR). Neither is the right index when your question is "what data exists where I can feed a stimulus into a foundation model and predict BOLD response?".

This repo answers that question across:

- **Static images** — NSD, THINGS-fMRI, BOLD5000, Generic Object Decoding…
- **Video clips** — BOLD Moments, vim-2, NFED…
- **Long-form film** — studyforrest, CNeuroMod Movie10, NNDb, Spacetop…
- **TV series** — CNeuroMod Friends…
- **Music** — Music Genre fMRI, studyforrest music…
- **Spoken language / podcasts / stories** — Narratives, LeBel Moth podcasts, Le Petit Prince…
- **Emotion-targeted** — Emo-FilM, NFED, NeuroEmo…
- **Decision / reward** — NARPS, HCP gambling…
- **Speech / motor production** — inner speech, motor imagery NF…
- **Video games / interactive** — CNeuroMod Mario, Shinobi…
- **Clinical populations** with task fMRI — UCLA CNP, AOMIC, HBN, ABIDE…
- **Mega-corpora & challenges** — Algonauts, TRIBE training mix, Neuroscout…

---

## How to use this catalog

- **`README.md` (this file)** — human-readable index, grouped by stimulus modality.
- **[`datasets.csv`](datasets.csv)** — single source of truth, one row per dataset. Use this to filter / join / build your own subsets.
- **[`POPULATION_MATRIX.md`](POPULATION_MATRIX.md)** — cross-table of *stimulus modality × population* showing coverage and gaps.
- **[`datasets.bib`](datasets.bib)** — BibTeX for every entry with a citation.
- **[`scripts/check_openneuro_status.py`](scripts/check_openneuro_status.py)** — pings the OpenNeuro API to refresh the `access` column.
- **[`CONTRIBUTING.md`](CONTRIBUTING.md)** — how to add a dataset (PRs welcome).

**Columns in `datasets.csv`:**

| Column | Meaning |
|---|---|
| `id` | short stable key, e.g. `nsd`, `bmd`, `cneuromod-friends` |
| `name` | canonical dataset name |
| `year` | primary publication / release year |
| `stimulus_modality` | image / video / film / tv / music / speech / decision / pain / motor / interactive / mixed |
| `population` | healthy-adult / healthy-aging / pediatric / asd / adhd / scz / mdd / ptsd / stroke / ad / mci / pain / addiction / mixed-clinical |
| `n_subjects` | total scanned |
| `n_unique_stimuli` | size of stimulus pool (`-` = continuous / single film) |
| `stimulus_repeats` | per-item repeats (`1` = no repeats, `3` = each shown ×3, `varies` = train/test split) |
| `hours_per_subject` | total fMRI time per participant |
| `field_strength` | 1.5T / 3T / 7T |
| `tr_seconds` | repetition time |
| `bids_compliant` | y / n / partial |
| `access` | open / openneuro / application / restricted |
| `licence` | data licence (CC-BY, CC-BY-SA, CC-BY-NC, custom, restricted) |
| `stimulus_licence` | stimulus-set licence (matters for downstream model release) |
| `url` | primary landing page |
| `doi` | dataset DOI when available |
| `used_in` | semicolon-separated list of notable papers/models |
| `notes` | one-liner gotchas |

---

## 1. Static image-presentation fMRI

The densest training data for image → BOLD models. Sort: chronological, newest first.

| Year | Dataset | N | Stimuli | Repeats | Hours/subj | Field | Access |
|---|---|---|---|---|---|---|---|
| 2025 | [CNeuroMod-THINGS](https://www.nature.com/articles/s41597-026-06591-y) | 4 | THINGS images | dense | very high | 3T | [CNeuroMod](https://github.com/courtois-neuromod/cneuromod) |
| 2023 | [Natural Object Dataset (NOD)](https://openneuro.org/datasets/ds004496) | 30 | ImageNet objects | multi | ~12 | 3T | OpenNeuro |
| 2023 | [THINGS-fMRI](https://openneuro.org/datasets/ds004192) | 3 (+4 v2) | 720 concepts / 8740 images | 12 sessions | ~12 | 3T (7T variant) | OpenNeuro |
| 2022 | [NSD (Natural Scenes Dataset)](https://naturalscenesdataset.org/) | 8 | ~73k COCO scenes | shared ×3, unique ×1 | 30–40 | 7T | Open (S3) |
| 2019 | [Deep Image Reconstruction](https://openneuro.org/datasets/ds001506) | 3 | 1200 train + 50 test ImageNet | train ×5, test ×24 | ~10 | 3T | OpenNeuro |
| 2018 | [BOLD5000](https://bold5000.github.io/) | 4 | 4916 images (COCO/ImageNet/Scene) | 15 sessions | ~20 | 3T | Open |
| 2017 | [Generic Object Decoding (Kamitani)](https://openneuro.org/datasets/ds001246) | 5 | 1250 ImageNet + imagery | train ×1, test ×35 | ~12 | 3T | OpenNeuro |
| 2008 | [vim-1 (Gallant)](https://crcns.org/data-sets/vc/vim-1) | 2 | 1750 train + 120 val natural | train ×2, val ×13 | — | 4T | CRCNS |
| 2001 | [Haxby ventral temporal](https://openneuro.org/datasets/ds000105) | 6 | 8 object categories | 12 runs/subj | — | 3T | OpenNeuro |

---

## 2. Video clips

Short dynamic stimuli with dense repeats — the natural extension of image datasets to motion.

| Year | Dataset | N | Stimuli | Repeats | Field | Access |
|---|---|---|---|---|---|---|
| 2024 | [BOLD Moments (BMD)](https://openneuro.org/datasets/ds005165) | 10 | 1102 × 3s videos (Memento10k) | train ×3, test ×10 | 3T | OpenNeuro |
| 2024 | [NFED (Natural Facial Expressions)](https://www.nature.com/articles/s41597-024-04088-0) | — | 1320 × 3s face videos | multi | 3T | OpenNeuro |
| 2023 | [vim-3](https://crcns.org/data-sets/vc/vim-3) | — | Natural movies | repeated | 7T | CRCNS |
| 2011 | [vim-2 (Gallant)](https://crcns.org/data-sets/vc/vim-2) | 3 | Natural movies | train long, test repeated | 4T | CRCNS |

---

## 3. Long-form film (single film, multi-session)

Reliability via ISC when there are no per-item repeats. Excellent for naturalistic encoders.

| Year | Dataset | N | Film | Hours | Field | Access |
|---|---|---|---|---|---|---|
| 2024 | [Spacetop](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12373947/) | 101 | Naturalistic + tasks (6h/subj) | 6 | 3T | Open |
| 2024 | [NNDb-3T+](https://www.naturalistic-neuroimaging-database.org/) | 40 | Back to the Future + retinotopy/somatotopy/tonotopy | full film | 3T | Open |
| 2023 | [NATVIEW EEG-fMRI](https://www.nature.com/articles/s41597-023-02458-8) | NKI | Movies + checkerboard + breath-hold | 2 sessions | 3T | Open |
| 2022 | [iEEG-fMRI short film](https://openneuro.org/datasets/ds003688) | 51 iEEG + 30 fMRI | "Pumzi" sci-fi 24-min | 0.4 | 3T | OpenNeuro |
| 2014–2021 | [studyforrest](https://www.studyforrest.org/) ([OpenNeuro ds000113](https://openneuro.org/datasets/ds000113)) | 20 | Forrest Gump audio (7T) + AV (3T) + retinotopy + localizers + music | ~8 | 7T+3T | OpenNeuro |

---

## 4. TV series (long arc, dense per-subject)

| Year | Dataset | N | Series | Hours | Access |
|---|---|---|---|---|---|
| 2018+ | [CNeuroMod Friends](https://github.com/courtois-neuromod/cneuromod) | 6 | Friends S1–S7 | up to 100+ | DataLad, open subset (sub-01/03/05) |
| 2018+ | [CNeuroMod Movie10](https://github.com/courtois-neuromod/cneuromod) | 6 | Bourne Supremacy, Hidden Figures, Life, Wolf of Wall Street | 10 | DataLad |

**Note:** Friends stimuli are proprietary — sharing trained model weights conditioned on these stimuli is fine, redistributing the videos is not. CNeuroMod provides BOLD; you provide the DVD.

---

## 5. Music / auditory (non-speech)

| Year | Dataset | N | Stimuli | Sessions | Access |
|---|---|---|---|---|---|
| 2021 | [Music Genre fMRI](https://openneuro.org/datasets/ds003720) | 5 | 10 genres × 540 clips × 15s | train/test split | OpenNeuro |
| 2014 | [studyforrest music](https://www.studyforrest.org/) | 20 | 25 segments × 5 genres | 8 runs | OpenNeuro |

**Gap:** no "NSD for music" exists yet — clear opportunity for new acquisition.

---

## 6. Spoken language / podcasts / stories

| Year | Dataset | N | Stimuli | Hours/subj | Access |
|---|---|---|---|---|---|
| 2023 | [LeBel / Moth podcast](https://openneuro.org/datasets/ds003020) | 8 | 27 Moth stories | ~6 | OpenNeuro |
| 2022 | [Le Petit Prince multilingual](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9424229/) | ~50/lang | The Little Prince audiobook EN/CN/FR | ~1.5 | OpenNeuro |
| 2021 | [Narratives](https://openneuro.org/datasets/ds002345) | 345 | 27 spoken stories (Sherlock, Merlin, Pieman…) | 0.5–2 | OpenNeuro |

---

## 7. Emotion-targeted

| Year | Dataset | N | Stimuli | Access |
|---|---|---|---|---|
| 2025 | [Emo-FilM](https://openneuro.org/datasets/ds004872) | 30 | 14 short emotional films + 50-item annotations | OpenNeuro |
| 2025 | [NeuroEmo](https://openneuro.org/datasets/ds005700) | — | Indian film clips, 5 emotions | OpenNeuro |
| 2024 | [NFED](https://www.nature.com/articles/s41597-024-04088-0) | — | 1320 face-expression videos | OpenNeuro |

---

## 8. Active task — decision / reward

| Year | Dataset | N | Task | Access |
|---|---|---|---|---|
| 2019 | [NARPS mixed gambles](https://openneuro.org/datasets/ds001734) | 108 | Mixed-gambles, 4 runs | OpenNeuro |
| 2024 | [Social Reward Young+Older](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10834522/) | — | Social reward decision | Application |
| 2013 | HCP gambling task | 1200 | Card-guessing | HCP application |

---

## 9. Active task — speech production / inner speech / motor imagery

| Year | Dataset | N | Task | Access |
|---|---|---|---|---|
| 2023 | [Bimodal EEG-fMRI inner speech](https://www.nature.com/articles/s41597-023-02286-w) | 3 | Inner repetition, 2 sessions | OpenNeuro |
| 2019 | [Simultaneous MRI-EEG motor imagery NF](https://www.biorxiv.org/content/10.1101/862375v1) | 30 | 5 NF training sessions | Open |

---

## 10. Video games / interactive

| Dataset | N | Game | Note |
|---|---|---|---|
| [CNeuroMod video games](https://github.com/courtois-neuromod/cneuromod) | 6 | Super Mario Bros, Shinobi III | First major "active" naturalistic corpus |

---

## 11. Clinical populations with rich task fMRI

Don't underestimate clinical data — heterogeneity is exactly the OOD test set foundation models need.

### 11.1 Transdiagnostic / multi-disorder

| Dataset | N | Diagnoses | Tasks | Access |
|---|---|---|---|---|
| [UCLA CNP / LA5c](https://openfmri.org/dataset/ds000030/) | 272 | HC + SCZ + BD + ADHD | 8 task batteries (stop-signal, BART, scap, PAMRet, PAMENC, taskswitch, BHT) | OpenNeuro, BIDS |
| [AOMIC PIOP1](https://openneuro.org/datasets/ds002785) | 216 | HC | Emotion matching, faces, stop-signal | OpenNeuro |
| [AOMIC PIOP2](https://openneuro.org/datasets/ds002790) | 226 | HC | Emotion matching, WM, stop-signal | OpenNeuro |
| [AOMIC ID1000](https://openneuro.org/datasets/ds003097) | 928 | HC population | Movie-watching | OpenNeuro |

### 11.2 By disorder

| Disorder | Datasets |
|---|---|
| **Schizophrenia / psychosis** | UCLA CNP, [COBRE](https://coins.trendscenter.org/), [B-SNIP](https://www.b-snip.org/), [HCP-EP](https://www.humanconnectome.org/study/human-connectome-project-for-early-psychosis), [fBIRN](https://www.nitrc.org/projects/fbirn/) |
| **Depression / mood** | [EMBARC](https://nda.nih.gov/edit_collection.html?id=2199), STRATIFY/ESTRA, CAN-BIND-1, OpenNeuro MDD studies |
| **Autism (ASD)** | [ABIDE-I/II](http://fcon_1000.projects.nitrc.org/indi/abide/), [EU-AIMS LEAP](https://www.aims-2-trials.eu/), [HBN](http://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/) |
| **ADHD** | [ADHD-200](http://fcon_1000.projects.nitrc.org/indi/adhd200/), UCLA CNP, Kessler response inhibition (Sci Data 2021) |
| **Stroke / aphasia** | ARC (Fridriksson), [PLORAS](https://www.fil.ion.ucl.ac.uk/ploras/), [ATLAS R2.0](http://fcon_1000.projects.nitrc.org/indi/retro/atlas.html) |
| **Pain** | [CoSpine](https://www.nature.com/articles/s41597-025-05982-x), [Wager self-regulation pain ds000140](https://openfmri.org/dataset/ds000140/), [OpenPain](http://www.openpain.org/) |
| **Addiction** | Stockholm Cocaine cohort, [NCANDA](https://www.niaaa.nih.gov/research/major-initiatives/national-consortium-alcohol-and-neurodevelopment-adolescence), ABCD substance subset |
| **PTSD / anxiety / OCD** | Trauma trajectories (Sheba), OCD task fMRI subsets on OpenNeuro |
| **AD / MCI task** | [PREVENT-AD task](https://openpreventad.loris.ca/), DELCODE, ADNI task subset |
| **Pediatric naturalistic** | [HBN](http://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/), [PIXAR Partly Cloudy ds000228](https://openneuro.org/datasets/ds000228), ABCD movie subset |

---

## 12. Mega-corpora, challenges & training mixes

| Year | Resource | What it bundles |
|---|---|---|
| 2026 | [TRIBE v2 (Meta FAIR)](https://huggingface.co/facebook/tribev2) | 1000+ h, 720 subj — NSD + CNeuroMod + Narratives + BMD + more. Weights CC-BY-NC |
| 2025 | [Algonauts 2025](https://algonautsproject.com/2025/) | CNeuroMod 80h × 4 subj (Friends S1–6 + Movie10) + OOD test |
| 2023 | [Algonauts 2023](http://algonauts.csail.mit.edu/) | NSD subset, image encoder benchmark |
| 2021 | [Algonauts 2021](http://algonauts.csail.mit.edu/2021/index.html) | BOLD Moments, video encoder benchmark |
| — | [Neuroscout](https://neuroscout.org/) | OpenNeuro + automated stimulus-feature extraction |
| — | [THINGS Initiative](https://things-initiative.org/) | THINGS-fMRI + THINGS-MEG + THINGS-EEG + behaviour |
| — | [CoRR](http://fcon_1000.projects.nitrc.org/indi/CoRR/html/) | 1629 reliability dataset aggregator |

---

## Known gaps (room for new acquisitions)

- **Music dense single-subject** (NSD-for-music) — doesn't exist.
- **Real-time conversation fMRI** — basically absent.
- **Long-form video game with behavioural log** — only CNeuroMod scratches it.
- **Sleep + dream-report fMRI** — fragmentary.
- **Tactile / olfactory naturalistic** — absent in open.
- **VR/AR immersive + fMRI** — single-site pilots only.
- **Open longitudinal task-fMRI in tumor / post-op** — structural exists (LUMIERE, UPENN-GBM), task does not.
- **MS task-fMRI longitudinal open** — MSSEG-1/2 is structural only.

---

## Related catalogs

- [multiBrain](https://github.com/Conxz/multiBrain) — dense single-subject / test-retest scans (the inspiration)
- [openneuro.org](https://openneuro.org/) — primary BIDS archive
- [CRCNS](https://crcns.org/) — Gallant lab, vim series
- [TCIA](https://www.cancerimagingarchive.net/) — neuro-oncology imaging
- [INDI / NITRC retro](http://fcon_1000.projects.nitrc.org/indi/) — ABIDE, ADHD-200, HBN, CoRR…

## Citing

If this catalog is useful in your work, please cite the underlying datasets (see [`datasets.bib`](datasets.bib)) — not this repo. The point of a catalog is to send credit where the data was collected.

## Licence

Catalog metadata is released under [CC0](LICENSE). Individual datasets retain their original licences (see `datasets.csv` → `licence` column).

---

## Pipeline (three-table schema)

The catalog uses a zero-trust three-table schema inspired by the [`healthaiatlas`](https://github.com/kondratevakate/healthaiatlas) data pipeline. Every claim about a dataset must cite a primary source URL.

```
data/
  entities.csv   — one row per dataset (id, name, url)
  claims.csv     — one factual claim per row (entity FK, predicate, value, source URL, confidence)
  sources.csv    — one URL per row (deduplicated, with liveness status)
  quarantine.csv — rows rejected during migration (audit only)
```

`datasets.csv` and `POPULATION_MATRIX.md` are **generated artifacts** — do not hand-edit them.

```bash
make migrate-apply   # flat datasets.csv → data/ (first time only)
make validate        # check invariants
make publish-apply   # data/ → regenerate datasets.csv + POPULATION_MATRIX.md
make verify-bib      # check datasets.bib against Crossref
```

See [`INCIDENTS.md`](INCIDENTS.md) for a production log of real failures and the hard rules that came out of them.
