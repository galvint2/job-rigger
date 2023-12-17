from pydantic import BaseModel, ConfigDict, Field, RootModel, field_validator

from job_rigger.utils import extract_entity_id


class JobSearchResult(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    reposted_job: bool = Field(..., alias="repostedJob")
    title: str
    poster_id: str = Field(..., alias="posterId")
    content_source: str = Field(..., alias="contentSource")
    entity_urn: str = Field(..., alias="entityUrn")

    @field_validator("entity_urn")
    @classmethod
    def extract_id_from_urn(cls, v: str) -> str:
        return extract_entity_id(v)


class JobSearchResultList(RootModel[list[JobSearchResult]]):
    root: list[JobSearchResult]
