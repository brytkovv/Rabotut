import re
from pydantic import BaseModel, validator, Field

'''Модель входящих данных'''


class Address(BaseModel):
    region: str
    city: str
    street_type: str
    street: str
    house_type: str
    house: str
    value: str
    lat: float = Field(ge=-90, le=90)
    lng: float = Field(ge=-180, le=180)


class Salary(BaseModel):
    from_: int = Field(alias='from')
    to: int
    currency: str
    gross: bool


class Contacts(BaseModel):
    fullName: str
    phone: str
    email: str

    @validator('phone')
    def phone_must_be_num(cls, v):
        if len(v) != 11 or not v.isnumeric():
            raise ValueError('Некорректный номер телефона')
        return v

    @validator('email')
    def email_must_contain_at(cls, v):
        if not re.fullmatch(r'.+@.+', v):
            raise ValueError('Некорректный емейл')
        return v


class IncomingData(BaseModel):
    description: str
    employment: str
    address: Address
    name: str
    salary: Salary
    contacts: Contacts


'''Модель результата'''


class Phone(BaseModel):
    city: str
    country: str
    number: str


class ResultContacts(BaseModel):
    email: str
    name: str
    phone: Phone


class ResultCoordinates(BaseModel):
    latitude: float
    longitude: float


class ResultExperience(BaseModel):
    id = "noMatter"


class ResultSalary_range(BaseModel):
    from_: int = Field(alias='from')
    to: int


class ResultSchedule(BaseModel):
    id: str


class ResultData(BaseModel):
    address: str
    allow_messages = True
    billing_type = "packageOrSingle"
    business_area = 1
    contacts: ResultContacts
    coordinates: ResultCoordinates
    description: str
    experience: ResultExperience
    html_tags = True
    image_url = "https://img.hhcdn.ru/employer-logo/3410666.jpeg"
    name: str
    salary: int
    salary_range: ResultSalary_range
    schedule: ResultSchedule
