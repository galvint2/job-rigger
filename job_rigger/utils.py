def extract_job_posting_id(entity_urn: str) -> str:
    job_posting_id = entity_urn.split(':')[-1]
    return job_posting_id
