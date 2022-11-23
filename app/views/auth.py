from datetime import datetime
from pydantic import BaseModel, HttpUrl, Field, constr


class ProfileView(BaseModel):
    first_name: constr() = Field(example='Иван')
    last_name: constr() = Field(example='Петров')
    login: str = Field(example='tagidick_tagidick')
    level: int = Field(description='Уровень пользователя', gt=0)
    image_url: HttpUrl = Field(example='https://pixelbox.ru/wp-content/uploads/2021/05/ava-vk-animal-91.jpg')
    updated_at: datetime
    created_at: datetime
