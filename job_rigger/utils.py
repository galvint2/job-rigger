from datetime import UTC, datetime


def extract_entity_id(entity_urn: str) -> str:
    job_posting_id = entity_urn.split(":")[-1]
    return job_posting_id


def timestamp_to_date(timestamp: int) -> str:
    return datetime.fromtimestamp(timestamp / 1000, UTC).strftime("%Y-%m-%d")
