# Phase One metadata builder

This directory builds deterministic, agent-readable metadata for every
authoritative PostGIS schema whose name starts with `a_`. It does not call an
LLM or any paid API.

## Production setup

1. Pull the repository onto the production server.
2. Create a virtual environment and install `requirements.txt`.
3. Copy `.env.example` to `.env` and provide the production PostGIS values.
4. Run the builder from the repository root:

```bash
python metadata_builder/build.py
```

The Linux convenience wrapper runs the same command:

```bash
metadata_builder/run_metadata_build.sh
```

## Useful commands

```bash
# No database connection; uses the three bundled development tables
python metadata_builder/build.py --mock

# Rebuild from an existing output/raw_schema.json
python metadata_builder/build.py --from-raw

# Process one schema
python metadata_builder/build.py --schema a_historic_england

# Ignore fingerprints and rebuild selected tables
python metadata_builder/build.py --schema a_historic_england --full-rebuild

# Retry tables named in the previous failure report
python metadata_builder/build.py --from-raw --retry-failed
```

Schema filters may be repeated. The default command connects to PostGIS and
processes all `a_*` schemas.

## Configuration committed to Git

- `config/sources.yml` maps schemas to publishers and official source pages.
- `config/column_dictionary.yml` provides reviewed common column meanings.
- `config/table_overrides.yml` contains table-specific titles, concepts and
  synonyms.
- `config/metadata_record.schema.json` documents the canonical record contract
  used by the later retrieval and tool-planning phases.

Unknown information is marked as unknown or needing review; the builder does
not invent licences or source facts.

Column semantics are resolved in this order: PostGIS comments, table-specific
configuration, schema-specific dictionaries, the global GIS dictionary,
structural patterns, then a safe unknown fallback. Records describe columns
independently using filter/search/join suitability, identifier systems,
geography hints, units, related coded-description fields, provenance and
confidence. They do not predefine table-to-table relationships. Later phases
will propose and validate relationships for the user's particular request.

PostgreSQL `pg_stats` supplies lightweight null/distinct hints where available.
Up to five bounded examples are collected only for text columns. These hints
support transparent relationship proposals but never prove a join by
themselves; Phase Three must validate proposed joins and ask the user to
confirm them.

## Generated outputs

- `output/metadata/*.json`: canonical full records.
- `output/tables/*.md`: readable documents rendered from the JSON.
- `output/agent_index.json`: compact retrieval index for the later planner.
- `output/build_state.json`: fingerprints used for incremental builds.
- `output/run_report.txt`: human-readable per-schema report.
- `output/run_report.json`: machine-readable report with detailed failures.

The output directory is intentionally ignored by Git because it is generated
from the environment-specific database. Code and configuration are pushed from
development; production pulls the code and builds its own current output.

## Success and failure accounting

A table is successful only when its canonical record validates and its JSON,
Markdown and index entry are available. The report lists, for every schema:

- tables found;
- successful/current tables;
- tables built in the current run;
- unchanged tables reused from a prior run;
- failed table names, stages and error messages.

One table failure does not stop the remaining tables. A fatal database or
configuration error stops the run with exit code 2. Completed runs containing
one or more table failures exit with code 1; fully successful runs exit with 0.

## Scheduling

Schedule the same production command with cron or a systemd timer. Start with a
weekly run. Fingerprints prevent unchanged tables from being regenerated. Logs
should be redirected outside the repository and monitored by the production
environment.
