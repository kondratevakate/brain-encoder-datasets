<!-- BEGIN AUTO-GENERATED POPULATION_MATRIX -->

| Population ↓ / Stimulus → | image | video | film | tv | music | speech | decision | pain | motor | interactive | mixed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **healthy-adult** | nsd, things-fmri, nod, bold5000, god-kamitani, deep-image-recon, vim-1, haxby-vt, cneuromod-things, algonauts-2023 | bmd, nfed, vim-2, vim-3, algonauts-2021 | studyforrest, nndb, spacetop, natview, cneuromod-movie10, emo-film, neuroemo, hcp-7t-movie, aomic-id1000, algonauts-2025 | cneuromod-friends | studyforrest-music, music-genre-fmri | narratives, lebel-moth, petit-prince, inner-speech-eegfmri | narps | cospine, wager-pain | motor-imagery-nf | cneuromod-games | hcp-task, aomic-piop1, aomic-piop2 |
| **healthy-aging** | — | — | — | — | — | — | social-reward | — | — | — | — |
| **pediatric** | — | — | pixar | — | — | — | — | — | — | — | hbn, abcd |
| **asd** | — | — | — | — | — | — | — | — | — | — | abide-1, abide-2 |
| **adhd** | — | — | — | — | — | — | — | — | — | — | adhd-200, kessler-inhibition |
| **scz** | — | — | — | — | — | — | — | — | — | — | hcp-ep, cobre-task, fbirn, b-snip |
| **mdd** | — | — | — | — | — | — | — | — | — | — | embarc |
| **stroke** | — | — | — | — | — | ploras | — | — | — | — | atlas-r2 |
| **mci** | — | — | — | — | — | — | — | — | — | — | prevent-ad-task |
| **addiction** | — | — | — | — | — | — | — | — | — | — | ncanda |
| **mixed-clinical** | — | — | ieeg-fmri-pumzi | — | — | — | — | — | — | — | ucla-cnp, tribe-v2 |

<!-- END AUTO-GENERATED POPULATION_MATRIX -->

# Population × Stimulus-Modality Coverage Matrix

A cross-table showing which populations have public fMRI data for which stimulus modalities. Empty cells = real gaps where new acquisitions would be valuable.

Cell contents are short dataset IDs from [`datasets.csv`](datasets.csv).

| Population ↓  /  Stimulus → | Static image | Video clip | Long-form film | TV series | Music | Speech / story | Emotion-targeted | Decision / reward | Pain | Motor / speech-prod | Interactive |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Healthy adult** | nsd, things-fmri, nod, bold5000, god-kamitani, deep-image-recon, vim-1, haxby-vt, cneuromod-things | bmd, nfed, vim-2, vim-3 | studyforrest, spacetop, nndb, natview, cneuromod-movie10 | cneuromod-friends | music-genre-fmri, studyforrest-music | narratives, lebel-moth, petit-prince | emo-film, neuroemo, nfed | narps, hcp-task | cospine, wager-pain | inner-speech-eegfmri, motor-imagery-nf | cneuromod-games |
| **Healthy aging** | — | — | spacetop (subset) | — | — | narratives (subset) | — | social-reward | — | — | — |
| **Pediatric typical** | — | — | aomic-id1000, pixar | — | — | — | — | abcd | — | — | — |
| **Pediatric clinical (HBN umbrella)** | — | — | hbn (Despicable Me, The Present) | — | — | — | — | hbn (MID) | — | — | — |
| **ASD** | — | — | hbn, abide-1/2 (site-dep) | — | — | narratives (subset) | — | — | — | — | — |
| **ADHD** | — | — | hbn | — | — | — | — | ucla-cnp, kessler-inhibition, adhd-200 | — | — | — |
| **Schizophrenia / psychosis** | — | — | hcp-ep | — | — | — | — | ucla-cnp, cobre-task, fbirn, b-snip, hcp-ep | — | — | — |
| **Bipolar** | — | — | — | — | — | — | — | ucla-cnp | — | — | — |
| **Depression (MDD)** | — | — | — | — | — | — | embarc | embarc | — | — | — |
| **PTSD / anxiety** | — | — | — | — | — | — | (Sheba trauma, restricted) | — | — | — | — |
| **Stroke / aphasia** | — | — | — | — | — | ploras, atlas-r2 (subset) | — | — | — | — | — |
| **Pain (chronic / acute)** | — | — | — | — | — | — | — | — | cospine, wager-pain, openpain.org collection | — | — |
| **Addiction** | — | — | — | — | — | — | — | ncanda, ABCD-substance | — | — | — |
| **AD / MCI** | — | — | — | — | — | — | — | prevent-ad-task | — | — | — |
| **Tumor pre/post-op** | — | — | — | — | — | (sparse language localizers in OpenNeuro) | — | — | — | (motor localizers, sparse) | — |
| **Multiple sclerosis** | — | — | — | — | — | — | — | — | — | — | — |

---

## Gaps worth highlighting

### High-value missing cells

| Cell | Why it matters |
|---|---|
| **Music × any clinical population** | We have no idea how music encoding differs in depression / ASD / SCZ. |
| **Static image × clinical** | The biggest encoder benchmarks (NSD, THINGS) are all 4–30 healthy young adults. No clinical OOD. |
| **Long-form film × MS / tumor longitudinal** | These populations have structural longitudinal but no task / naturalistic. |
| **Interactive (games) × anything beyond CNeuroMod** | Active naturalistic in only one cohort, 6 people. |
| **Tactile / olfactory / VR / multi-person hyperscanning** | Whole columns missing from the table — would each be its own new acquisition direction. |

### Where coverage is good

- **Static image × healthy adult** — saturated; new acquisitions here probably need a novel twist (clinical, music-equivalent, etc.).
- **Decision / reward × mixed-clinical** — UCLA CNP is the workhorse and covers most major adult disorders.
- **Long-form film × pediatric** — HBN + Pixar + ABCD give 17k+ kids.

---

## How to use this matrix

- **Looking for OOD test data?** Pick a row your model wasn't trained on.
- **Designing an acquisition?** Pick an empty cell that aligns with your scientific question.
- **Building a multi-population encoder?** Read each row to see which modalities you can stack within one population.

When updating: keep cells short (dataset IDs only), put long context in the README section, and add new dataset IDs to [`datasets.csv`](datasets.csv) so the matrix stays grep-able against the source of truth.
