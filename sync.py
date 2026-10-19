import argparse
import logging
from datetime import datetime, timedelta
from syncer import CRMSyncer

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('sync.log'),
    ]
)
log = logging.getLogger(__name__)

def parse_since(since_str: str) -> datetime:
    if since_str.endswith('h'):
        return datetime.utcnow() - timedelta(hours=int(since_str[:-1]))
    if since_str.endswith('d'):
        return datetime.utcnow() - timedelta(days=int(since_str[:-1]))
    return datetime.fromisoformat(since_str)

def main():
    parser = argparse.ArgumentParser(description='CRM Sync Tool')
    parser.add_argument('--direction', choices=['push', 'pull', 'both'], default='both')
    parser.add_argument('--entity', choices=['contacts', 'companies', 'deals'], required=True)
    parser.add_argument('--since', default=None, help='Incremental sync since (e.g. 24h, 7d, 2024-01-01)')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without applying')
    args = parser.parse_args()

    since = parse_since(args.since) if args.since else None

    log.info(f"Starting CRM sync | entity={args.entity} direction={args.direction} since={since} dry_run={args.dry_run}")
    syncer = CRMSyncer(entity=args.entity, dry_run=args.dry_run)

    if args.direction in ('pull', 'both'):
        pulled = syncer.pull(since=since)
        log.info(f"Pulled {pulled} records from CRM")

    if args.direction in ('push', 'both'):
        pushed = syncer.push(since=since)
        log.info(f"Pushed {pushed} records to CRM")

    log.info("Sync complete.")

if __name__ == '__main__':
    main()