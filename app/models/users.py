from models.base import BaseWithDatetime
from tortoise import fields


class User(BaseWithDatetime):
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255)
    login = fields.CharField(max_length=50)
    level = fields.SmallIntField()
    image_url = fields.CharField(max_length=255)

    class Meta:
        table = "users"
