from typing import List

from pydantic import BaseModel, Field, field_validator

from .utils import extract_job_posting_id


class JobPosting(BaseModel):
    trackingUrn: str = Field(..., alias='trackingUrn')
    repostedJob: bool = Field(..., alias='repostedJob')
    title: str = Field(..., alias='title')
    recipeTypes: List[str] = Field(..., alias='$recipeTypes')
    posterId: str = Field(..., alias='posterId')
    contentType: str = Field(..., alias='contentSource')
    entityUrn: str = Field(..., alias='entityUrn')

    @field_validator('entityUrn')
    def extract_id_from_urn(cls, v: str) -> str:
        return extract_job_posting_id(v)


class JobPostingList(BaseModel):
    job_postings: List[JobPosting]
