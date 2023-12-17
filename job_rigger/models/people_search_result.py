from pydantic import BaseModel, ConfigDict


class PeopleSearchResult(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    urn_id: str
    distance: str
    jobtitle: str
    location: str
    name: str


class PeopleSearchResultList(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    results: list[PeopleSearchResult]
