from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CompanyResolutionResult(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    entity_urn: str = Field(..., alias="entityUrn")
    name: str
    universal_name: str = Field(..., alias="universalName")
    url: str


class JobPostingCompany(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    company_resolution_result: CompanyResolutionResult = Field(..., alias="companyResolutionResult")
    company: str


class CompanyDetails(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    job_posting_company: JobPostingCompany = Field(
        ..., alias="com.linkedin.voyager.deco.jobs.web.shared.WebCompactJobPostingCompany"
    )


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


class ComLinkedinVoyagerJobsComplexOnsiteApply(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    unify_apply_enabled: bool = Field(..., alias="unifyApplyEnabled")
    easy_apply_url: str = Field(..., alias="easyApplyUrl")
    company_apply_url: Optional[str] = Field(None, alias="companyApplyUrl")


class ComLinkedinVoyagerJobsSimpleOnsiteApply(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    unify_apply_enabled: bool = Field(..., alias="unifyApplyEnabled")


class ApplyMethod(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    com_linkedin_voyager_jobs_offsite_apply: Optional[ComLinkedinVoyagerJobsOffsiteApply] = Field(
        None, alias="com.linkedin.voyager.jobs.OffsiteApply"
    )
    com_linkedin_voyager_jobs_complex_onsite_apply: Optional[ComLinkedinVoyagerJobsComplexOnsiteApply] = Field(
        None, alias="com.linkedin.voyager.jobs.ComplexOnsiteApply"
    )
    com_linkedin_voyager_jobs_simple_onsite_apply: Optional[ComLinkedinVoyagerJobsSimpleOnsiteApply] = Field(
        None, alias="com.linkedin.voyager.jobs.SimpleOnsiteApply"
    )


class UrnLiFsWorkplaceType1(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    localized_name: str = Field(..., alias="localizedName")
    entity_urn: str = Field(..., alias="entityUrn")


class UrnLiFsWorkplaceType2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    localized_name: str = Field(..., alias="localizedName")
    entity_urn: str = Field(..., alias="entityUrn")


class UrnLiFsWorkplaceType3(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    localized_name: str = Field(..., alias="localizedName")
    entity_urn: str = Field(..., alias="entityUrn")


class WorkplaceTypesResolutionResults(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    urn_li_fs_workplace_type_1: Optional[UrnLiFsWorkplaceType1] = Field(None, alias="urn:li:fs_workplaceType:1")
    urn_li_fs_workplace_type_3: Optional[UrnLiFsWorkplaceType3] = Field(None, alias="urn:li:fs_workplaceType:3")
    urn_li_fs_workplace_type_2: Optional[UrnLiFsWorkplaceType2] = Field(None, alias="urn:li:fs_workplaceType:2")


class JobDetail(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    title: str
    description: Description
    company_details: CompanyDetails = Field(..., alias="companyDetails")
    job_state: str = Field(..., alias="jobState")
    entity_urn: str = Field(..., alias="entityUrn")
    work_remote_allowed: bool = Field(..., alias="workRemoteAllowed")
    apply_method: ApplyMethod = Field(..., alias="applyMethod")
    talent_hub_job: bool = Field(..., alias="talentHubJob")
    formatted_location: str = Field(..., alias="formattedLocation")
    workplace_types: list[str] = Field(..., alias="workplaceTypes")
    listed_at: int = Field(..., alias="listedAt")
    job_posting_id: int = Field(..., alias="jobPostingId")
    workplace_types_resolution_results: Optional[WorkplaceTypesResolutionResults] = Field(
        None, alias="workplaceTypesResolutionResults"
    )


class JobDetailList(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    results: list[JobDetail]
