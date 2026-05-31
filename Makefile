# brain-encoder-datasets catalog pipeline
# -----------------------------------------
# make migrate          -- dry-run migration from datasets.csv → data/
# make migrate-apply    -- run migration for real
# make validate         -- check invariants
# make publish          -- dry-run publish (regenerate flat CSV + matrix)
# make publish-apply    -- regenerate for real
# make verify-bib       -- check datasets.bib against Crossref
# make all              -- migrate-apply → validate → publish-apply

PYTHON = python

.PHONY: migrate migrate-apply validate publish publish-apply verify-bib all

migrate:
	$(PYTHON) -m pipeline.migrate

migrate-apply:
	$(PYTHON) -m pipeline.migrate --apply --backup

validate:
	$(PYTHON) -m pipeline.validate

validate-strict:
	$(PYTHON) -m pipeline.validate --strict

publish:
	$(PYTHON) -m pipeline.publish

publish-apply:
	$(PYTHON) -m pipeline.publish --apply

verify-urls:
	$(PYTHON) -m pipeline.verify

verify-urls-apply:
	$(PYTHON) -m pipeline.verify --apply

verify-urls-stale:
	$(PYTHON) -m pipeline.verify --older-than 90 --apply

verify-bib:
	$(PYTHON) "$(shell python -c "import os; print(os.path.expanduser('~/.claude/skills/bib-verify/scripts/verify_bib.py'))")" \
		datasets.bib --out "verification/$$(date +%Y-%m-%d)_bib_check.md" --fix
	@echo "Report written to verification/"

all: migrate-apply validate publish-apply
	@echo "Pipeline complete."
