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
| 2023 | [**devCCNP (Chinese Color Nest)**](https://www.nature.com/articles/s41597-023-02377-8) | 369 (6–17 yr) | Naturalistic viewing + rsfMRI + multi-modal, **3 waves longitudinal** | varies | 3T | National Science Data Bank — first major Chinese pediatric naturalistic-viewing resource |
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
| [**SRPBS Multi-disorder MRI**](https://bicr-resource.atr.jp/srpbsopen/) | **993 patients + 1421 HC** | MDD + SCZ + ASD + OCD across 12 Japanese sites | T1 + rsfMRI + task subsets | ATR application (Tanaka et al., Sci Data 2021) |
| [**SRPBS Traveling Subject MRI**](https://bicr-resource.atr.jp/srpbsts/) | 9 × 12 scanners | Healthy traveling | T1 + rsfMRI, 143 sessions | ATR application — Asia harmonization backbone |
| [AOMIC PIOP1](https://openneuro.org/datasets/ds002785) | 216 | HC | Emotion matching, faces, stop-signal | OpenNeuro |
| [AOMIC PIOP2](https://openneuro.org/datasets/ds002790) | 226 | HC | Emotion matching, WM, stop-signal | OpenNeuro |
| [AOMIC ID1000](https://openneuro.org/datasets/ds003097) | 928 | HC population | Movie-watching | OpenNeuro |
| [**Ge 2022 Chinese multi-modal**](https://www.nature.com/articles/s41597-022-01413-3) | 215 healthy Chinese | HC diversity | T1 + rsfMRI + dMRI | Open via paper |

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
| **AD / MCI task** | [PREVENT-AD task](https://openpreventad.loris.ca/), DELCODE, ADNI task subset, [**KBASE (Korea, SNU)**](https://dss.niagads.org/cohorts/korean-brain-aging-study-for-the-early-diagnosis-and-prediction-of-ad-kbase/), [**J-ADNI (Japan, NBDC)**](https://humandbs.dbcls.jp/en/hum0043-v1) |
| **Pediatric naturalistic** | [HBN](http://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/), [PIXAR Partly Cloudy ds000228](https://openneuro.org/datasets/ds000228), ABCD movie subset, [**devCCNP (China)**](https://www.nature.com/articles/s41597-023-02377-8) |
| **Population diversity (non-Western)** | [**CHIMGEN (China, 7000+)**](https://www.nature.com/articles/s41380-019-0627-6) — multimodal incl. rsfMRI; mostly out-of-scope for stimulus-locked but useful for HC pretraining |

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

## 13. Asian-population coverage (explicit fix for Western bias)

Most fMRI catalogs — including earlier versions of this one — are heavily Western. That matters because (a) brain-age and encoder generalization fail across populations, (b) Asian neuroimaging consortia are large but often hosted on local repositories rather than OpenNeuro, and (c) several major resources are misattributed (e.g. NOD is BNU, not Western). This section flags what's specifically Asian and why each is or isn't in the main tables above.

### In-scope for this catalog (stimulus-locked / task)

| Dataset | Country | Where in this README |
|---|---|---|
| [Natural Object Dataset (NOD)](https://openneuro.org/datasets/ds004496) | 🇨🇳 China (BNU, Beijing) | §1 — Chinese image-encoding workhorse, ~30 subjects ImageNet |
| [Le Petit Prince multilingual](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9424229/) | 🇨🇳 CN + 🇫🇷 FR + 🇺🇸 EN | §6 — includes Mandarin Chinese subset (~50 subjects) |
| [devCCNP](https://www.nature.com/articles/s41597-023-02377-8) | 🇨🇳 China (BNU + CAS) | §3 — naturalistic viewing in pediatric Chinese; 3 longitudinal waves |
| [SRPBS Multi-disorder MRI](https://bicr-resource.atr.jp/srpbsopen/) | 🇯🇵 Japan (ATR + 12 sites) | §11.1 — 993 patients + 1421 HC across MDD/SCZ/ASD/OCD |
| [SRPBS Traveling Subject MRI](https://bicr-resource.atr.jp/srpbsts/) | 🇯🇵 Japan | §11.1 — Asia's answer to ON-Harmony/DecNef |
| [Ge 2022 Chinese multi-modal](https://www.nature.com/articles/s41597-022-01413-3) | 🇨🇳 China | §11.1 — 215 healthy Chinese, T1+rsfMRI+dMRI |
| [KBASE](https://dss.niagads.org/cohorts/korean-brain-aging-study-for-the-early-diagnosis-and-prediction-of-ad-kbase/) | 🇰🇷 Korea (SNU) | §11.2 — Korean ADNI, task fMRI in MCI/AD |
| [J-ADNI](https://humandbs.dbcls.jp/en/hum0043-v1) | 🇯🇵 Japan (NBDC) | §11.2 — Japanese ADNI mirror |
| [NeuroEmo](https://openneuro.org/datasets/ds005700) | 🇮🇳 India | §7 — Indian film clips for emotion categories |

### Adjacent — out of scope here, but flagged for use as HC pretraining / test-retest

These are mostly resting-state or pure structural and don't fit the stimulus-locked criterion, but they're the largest Asian cohorts and important pretraining material:

| Dataset | Country | N | Why not in main tables |
|---|---|---|---|
| [CHIMGEN](https://www.nature.com/articles/s41380-019-0627-6) | 🇨🇳 China, 33 centers | 7000+ (10k target) | T1 + DTI + rsfMRI primarily; no native task encoder use |
| [CCNP matCCNP / ageCCNP](https://pmc.ncbi.nlm.nih.gov/articles/PMC8517840/) | 🇨🇳 China | 560 + 480 | Adult / aging waves are mostly rsfMRI |
| [SLIM (Southwest U Longitudinal)](http://fcon_1000.projects.nitrc.org/indi/retro/southwestuni_qiu_index.html) | 🇨🇳 China (Chongqing) | ~600 students × 3 waves | T1 + rsfMRI; great for retest, no stimulus |
| [SALD (Southwest U Adult Lifespan)](http://fcon_1000.projects.nitrc.org/indi/retro/sald.html) | 🇨🇳 China (Chongqing) | 494 (19–80 yr) | sMRI + rsfMRI cross-sectional |
| [HNU / CCBD (Hangzhou Normal U)](https://doi.org/10.6084/m9.figshare.2007483) | 🇨🇳 China | 30 × 10 scans | Densest Chinese T1 test-retest; rsfMRI only |
| [BNU 1 / 2 / 3 + IPCAS 1–8](https://fcon_1000.projects.nitrc.org/indi/CoRR/html/samples.html) | 🇨🇳 China | aggregated in [CoRR](http://fcon_1000.projects.nitrc.org/indi/CoRR/html/) | Test-retest only; ~⅓ of CoRR is Asian and underacknowledged |
| [Korean Brain Aging single-scanner 1000+](https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2020.00233/full) | 🇰🇷 Korea | 1000+ elderly | Single-scanner T1 + cognition; aging study |
| [TWBB (Taiwan Biobank imaging arm)](https://www.twbiobank.org.tw/) | 🇹🇼 Taiwan | ~2000 | Population imaging, structural focus |

### Why the gap exists

- Asian datasets often live on **local repositories** (`bicr-resource.atr.jp` for SRPBS, `humandbs.dbcls.jp` for J-ADNI, National Science Data Bank for CCNP) rather than OpenNeuro, so OpenNeuro-only searches miss them entirely.
- **CoRR aggregator hides per-site origin** — ~⅓ of its 1629 subjects are from Chinese sites (BNU, IPCAS, SWU) but the consortium-level branding obscures this. Always check the per-site documentation, not just the umbrella name.
- **DecNef / SRPBS terminology confusion**: what's often cited as "DecNef" travelling-subjects is actually one component of the broader SRPBS family. Four datasets share the same application form.
- **Westerncentric naming bias in landmark datasets**: NOD (Beijing Normal U), CCNP (BNU + CAS), Ge 2022 are sometimes cited without country attribution, contributing to invisibility.

### Population atlas for Asian cohorts

If you train on Asian data, use Asian-derived templates rather than MNI152:

- [**CHN-PD (Chinese Pediatric Atlas)**](https://www.biorxiv.org/content/10.1101/385211.full.pdf) — 328 children at 3T Prisma, BNU
- [**Chinese 2020 adult atlas**](https://www.nature.com/articles/srep18216) — multi-center, 18–76 yr
- [**Brainnetome Atlas**](https://atlas.brainnetome.org/) — Chinese parcellation reference

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
