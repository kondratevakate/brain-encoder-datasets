"""
Dataclasses for the three-table normalized schema.

entities  — one row per dataset (id + canonical name + url)
claims    — one factual claim per row (entity FK + predicate + value + source)
sources   — one URL per row (deduplicated across all claims)

Generated flat datasets.csv is a derived artifact produced by
pipeline/publish.py and should NOT be hand-edited.
"""
from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Entity:
    entity_id: str       # stable slug, e.g. 'nsd', 'bmd'
    name: str            # canonical display name
    url: str             # primary landing page (required, verified)


@dataclass
class Source:
    source_id: str       # slug derived from URL (sha8 of url)
    url: str             # primary URL (must be non-empty)
    retrieved_at: str    # ISO date when last verified, e.g. '2026-05-31'
    wayback_url: str = ""  # fallback URL if primary is dead
    status: str = "ok"   # 'ok' / 'dead' / 'redirect' / 'unverified'


@dataclass
class Claim:
    claim_id: str         # '{entity_id}__{predicate}' (unique per entity)
    entity_id: str        # FK → Entity.entity_id
    predicate: str        # from schema.predicates (locked enum)
    value: str            # the fact value
    source_ids: list[str] = field(default_factory=list)  # FK → Source.source_id
    confidence: str = "high"   # 'high' / 'medium' / 'low' / 'unverified'
    retrieved_at: str = ""     # ISO date when this claim was last checked


# Column orders for CSV I/O
ENTITY_COLUMNS = ["entity_id", "name", "url"]

SOURCE_COLUMNS = ["source_id", "url", "retrieved_at", "wayback_url", "status"]

CLAIM_COLUMNS = [
    "claim_id", "entity_id", "predicate", "value",
    "source_ids",   # stored as semicolon-separated source_ids
    "confidence", "retrieved_at",
]
