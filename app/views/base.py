from typing import TypeVar

from starlette.status import HTTP_200_OK

from pydantic import Field
from pydantic.schema import Generic
from pydantic.generics import GenericModel


DataT = TypeVar('DataT')


class Response(GenericModel, Generic[DataT]):
    """
        Базовый ответ на запрос
    """
    code: int = Field(HTTP_200_OK, description='Код ответа (http-like)')
    message: str | None = Field("OK", description='Описание кода ответа')
    payload: DataT | None = Field(description='Тело ответа')