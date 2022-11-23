from typing import Any, Mapping

from starlette import status


class ApiException(Exception):
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    message: str = 'Упс! Что-то пошло не так ;('

    def __init__(self, message: str | None = None, payload: Mapping | None = None, debug: Any = None):
        self.message = message or self.message
        self.payload = payload

    def to_json(self) -> Mapping:
        return {
            'code': self.status_code,
            'message': self.message,
            'payload': self.payload
        }


class ServerError(ApiException):
    status_code = 500
    message = 'Упс! Что-то пошло не так ;('


class NotFoundError(ApiException):
    status_code = 404
    message = 'Not Found'