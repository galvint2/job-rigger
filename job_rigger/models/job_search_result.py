from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from job_rigger.utils import extract_entity_id


class JobSearchResult(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    title: str
    entity_urn: str = Field(..., alias="entityUrn")
    reposted_job: bool = Field(..., alias="repostedJob")
    poster_id: Optional[str] = Field(..., alias="posterId")
    content_source: str = Field(..., alias="contentSource")

    @field_validator("entity_urn")
    @classmethod
    def extract_id_from_urn(cls, v: str) -> str:
        return extract_entity_id(v)


class JobSearchResults(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    results: list[JobSearchResult]
