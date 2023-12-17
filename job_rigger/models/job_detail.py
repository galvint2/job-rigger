from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from job_rigger.utils import extract_entity_id, timestamp_to_date


class CompanyResolutionResult(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    entity_urn: str = Field(..., alias="companyEntityUrn")
    name: str
    universal_name: str = Field(..., alias="universalName")
    url: str


class JobPostingCompany(BaseModel):
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
    job_posting_company: JobPostingCompany = Field(..., alias="jobPostingCompany")


class Description(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    text: str


class OffsiteApply(BaseModel):
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
    offsite_apply: OffsiteApply = Field(..., alias="com.linkedin.voyager.jobs.OffsiteApply")


class JobDetail(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="ignore")
    title: str
    description: Description
    work_remote_allowed: bool = Field(..., alias="workRemoteAllowed")
    location: str = Field(..., alias="formattedLocation")
    job_state: str = Field(..., alias="jobState")
    entity_urn: str = Field(..., alias="entityUrn")
    company_entity_urn: str = Field(..., alias="companyEntityUrn")
    company_name: str = Field(..., alias="name")
    company_universal_name: str = Field(..., alias="universalName")
    company_url: str = Field(..., alias="url")
    company_apply_url: ApplyMethod = Field(..., alias="applyMethod")
    talent_hub_job: bool = Field(..., alias="talentHubJob")
    listed_at: int = Field(..., alias="listedAt")

    @field_validator("company_apply_url")
    @classmethod
    def unnest_apply_method(cls, v: ApplyMethod) -> str:
        return v.offsite_apply.company_apply_url

    @field_validator("description")
    @classmethod
    def unnest_description(cls, v: Description) -> str:
        return v.text

    @field_validator("listed_at")
    @classmethod
    def convert_timestamp(cls, v: int) -> str:
        return timestamp_to_date(v)

    @field_validator("entity_urn")
    @classmethod
    def extract_id_from_urn(cls, v: str) -> str:
        return extract_entity_id(v)

    @model_validator(mode="before")
    @classmethod
    def extract_company_resolution_result(cls, values):
        company_details = values.get("companyDetails")
        job_posting_company = company_details.get(
            "com.linkedin.voyager.deco.jobs.web.shared.WebCompactJobPostingCompany"
        )
        company_resolution_result = job_posting_company.get("companyResolutionResult")
        values["name"] = company_resolution_result.get("name", "")
        values["company_universal_name"] = company_resolution_result.get("universalName", "")
        values["url"] = company_resolution_result.get("url", "")
        company_entity_urn = company_resolution_result.get("entityUrn", "")
        values["company_entity_urn"] = extract_entity_id(company_entity_urn)

        return values
