# crm-sync-tool

Bidirectional CRM data synchronization tool for B2B enterprise workflows. Syncs contacts, companies, and deal pipelines between internal databases and CRM platforms (HubSpot / Salesforce).

## Features
- Bidirectional sync: local DB <-> CRM platform
- Conflict resolution (last-write-wins or manual)
- Field mapping configuration (YAML)
- Incremental sync (only changed records)
- Sync audit log

## Quick Start
```bash
pip install -r requirements.txt
cp config.example.yaml config.yaml
# Configure your CRM credentials and field mappings

# Full sync
python sync.py --direction both --entity contacts

# Incremental sync (last 24h)
python sync.py --direction push --entity deals --since 24h
```

## Supported Platforms
- HubSpot CRM (via API v3)
- Salesforce (via REST API)
- Extensible via base adapter

## Tech Stack
- Python 3.10+
- requests, pyyaml
- SQLite / PostgreSQL
- Logging + audit trail