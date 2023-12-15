from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from job_rigger.utils import extract_entity_id


class CompanyResolutionResult(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    entity_urn: str = Field(..., alias="entityUrn")
    name: str
    recipe_type: str = Field(..., alias="$recipeType")
    universal_name: str = Field(..., alias="universalName")
    url: str


class ComLinkedinVoyagerDecoJobsWebSharedWebCompactJobPostingCompany(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    company_resolution_result: CompanyResolutionResult = Field(..., alias="companyResolutionResult")
    company: str
    recipe_type: str = Field(..., alias="$recipeType")


class CompanyDetails(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    com_linkedin_voyager_deco_jobs_web_shared_web_compact_job_posting_company: ComLinkedinVoyagerDecoJobsWebSharedWebCompactJobPostingCompany = Field(
        ..., alias="com.linkedin.voyager.deco.jobs.web.shared.WebCompactJobPostingCompany"
    )


class ComLinkedinPemberlyTextList(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    ordered: bool


class ListModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    ordered: bool


class AttributeKindUnion(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    bold: Optional[dict[str, Any]] = None
    paragraph: Optional[dict[str, Any]] = None
    line_break: Optional[dict[str, Any]] = Field(None, alias="lineBreak")
    list_item: Optional[dict[str, Any]] = Field(None, alias="listItem")
    list: Optional[ListModel] = None
    italic: Optional[dict[str, Any]] = None


class Description(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    text: str


class ComLinkedinVoyagerJobsOffsiteApply(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    apply_starters_preference_void: bool = Field(..., alias="applyStartersPreferenceVoid")
    company_apply_url: str = Field(..., alias="companyApplyUrl")
    in_page_offsite_apply: bool = Field(..., alias="inPageOffsiteApply")


class ApplyMethod(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    com_linkedin_voyager_jobs_offsite_apply: ComLinkedinVoyagerJobsOffsiteApply = Field(
        ..., alias="com.linkedin.voyager.jobs.OffsiteApply"
    )


class UrnLiFsWorkplaceType3(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    localized_name: str = Field(..., alias="localizedName")
    recipe_type: str = Field(..., alias="$recipeType")
    entity_urn: str = Field(..., alias="entityUrn")


class WorkplaceTypesResolutionResults(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    urn_li_fs_workplace_type_3: UrnLiFsWorkplaceType3 = Field(..., alias="urn:li:fs_workplaceType:3")


class JobDetail(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    company_details: CompanyDetails = Field(..., alias="companyDetails")
    job_state: str = Field(..., alias="jobState")
    description: Description
    title: str
    entity_urn: str = Field(..., alias="entityUrn")
    work_remote_allowed: bool = Field(..., alias="workRemoteAllowed")
    apply_method: ApplyMethod = Field(..., alias="applyMethod")
    talent_hub_job: bool = Field(..., alias="talentHubJob")
    location: str = Field(..., alias="formattedLocation")
    workplace_types: list[str] = Field(..., alias="workplaceTypes")
    listed_at: int = Field(..., alias="listedAt")
    job_posting_id: int = Field(..., alias="jobPostingId")
    workplace_types_resolution_results: WorkplaceTypesResolutionResults = Field(
        ..., alias="workplaceTypesResolutionResults"
    )

    # @field_validator("job_posting_id")
    # def extract_job_posting_id(cls, v: str) -> str:
    #     return extract_entity_id(v)

    @field_validator("entity_urn")
    def extract_entity_urn(cls, v: str) -> str:
        return extract_entity_id(v)
