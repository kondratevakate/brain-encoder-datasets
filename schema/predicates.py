"""
Locked predicate vocabulary for brain-encoder-datasets claims.

Every claim in claims.csv must use one of these predicate names.
Adding a new predicate requires a reviewer sign-off and an update to
this file — they propagate to downstream tools (validate, publish, UI).

Do NOT add predicates that are free-form text (use `notes` for that).
Each predicate should be a single falsifiable fact about one dataset.
"""

# --- Structural facts ---
YEAR = "year"                       # int: primary publication / release year
N_SUBJECTS = "n_subjects"           # int or '-': number of scanned subjects
N_UNIQUE_STIMULI = "n_unique_stimuli"  # int or '-': unique items in stimulus pool
STIMULUS_REPEATS = "stimulus_repeats"  # str: e.g. '3' / 'train-x5-test-x24' / 'varies'
HOURS_PER_SUBJECT = "hours_per_subject"  # str: total scanning hours per participant
FIELD_STRENGTH = "field_strength"   # enum: '1.5T' / '3T' / '4T' / '7T' / 'mixed'
TR_SECONDS = "tr_seconds"           # float: repetition time in seconds

# --- Classification ---
STIMULUS_MODALITY = "stimulus_modality"   # enum (see STIMULUS_MODALITY_VALUES)
POPULATION = "population"                 # enum (see POPULATION_VALUES)

# --- Access / compliance ---
BIDS_COMPLIANT = "bids_compliant"   # enum: 'y' / 'n' / 'partial'
ACCESS = "access"                   # enum (see ACCESS_VALUES)
LICENCE = "licence"                 # str: CC-BY-4.0, CC0, custom-DUA, restricted…
STIMULUS_LICENCE = "stimulus_licence"  # str: licence of the stimulus material itself

# --- Provenance ---
URL = "url"                         # str: primary landing page (required)
DOI = "doi"                         # str: dataset DOI when available
USED_IN = "used_in"                 # str: semicolon-separated papers/models

# --- Narrative ---
NOTES = "notes"                     # str: one-liner gotchas (free text, one per entity)

# Ordered list for canonical column order in generated CSVs
ALL_PREDICATES = [
    YEAR, STIMULUS_MODALITY, POPULATION,
    N_SUBJECTS, N_UNIQUE_STIMULI, STIMULUS_REPEATS, HOURS_PER_SUBJECT,
    FIELD_STRENGTH, TR_SECONDS,
    BIDS_COMPLIANT, ACCESS, LICENCE, STIMULUS_LICENCE,
    URL, DOI, USED_IN, NOTES,
]

# ---- Locked enum values ----

STIMULUS_MODALITY_VALUES = frozenset({
    "image", "video", "film", "tv", "music", "speech",
    "decision", "pain", "motor", "interactive", "mixed",
})

POPULATION_VALUES = frozenset({
    "healthy-adult", "healthy-aging", "pediatric",
    "asd", "adhd", "scz", "mdd", "ptsd",
    "stroke", "ad", "mci", "pain", "addiction",
    "mixed-clinical",
})

ACCESS_VALUES = frozenset({
    "open", "openneuro", "application", "restricted",
})

BIDS_VALUES = frozenset({"y", "n", "partial"})

FIELD_STRENGTH_VALUES = frozenset({"0.064T", "1.5T", "3T", "4T", "7T", "mixed"})

CONFIDENCE_VALUES = frozenset({"high", "medium", "low", "unverified"})

# Predicates that must have source_url (confidence ≥ medium) when set
SOURCED_PREDICATES = frozenset({
    YEAR, N_SUBJECTS, N_UNIQUE_STIMULI, HOURS_PER_SUBJECT,
    ACCESS, LICENCE, STIMULUS_LICENCE, DOI,
})

# Predicates where source_url = '' is acceptable (structural / editorial)
UNSOURCED_OK_PREDICATES = frozenset({
    STIMULUS_MODALITY, POPULATION, BIDS_COMPLIANT,
    FIELD_STRENGTH, TR_SECONDS, STIMULUS_REPEATS,
    USED_IN, NOTES, URL,
})
