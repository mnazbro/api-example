# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .movie_id import MovieId


class Movie(pydantic.BaseModel):
    id: MovieId
    title: str
    rating: float = pydantic.Field(description=("The rating scale is one to five stars\n"))

    class Partial(typing_extensions.TypedDict):
        id: typing_extensions.NotRequired[MovieId]
        title: typing_extensions.NotRequired[str]
        rating: typing_extensions.NotRequired[float]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
