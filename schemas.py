from datetime import datetime, date
from pydantic import BaseModel, constr
from typing import List, Optional, Dict, Text
from enum import Enum
from sqlalchemy.types import UserDefinedType

class Actor(BaseModel):
    actor_id: int
    first_name: constr(max_length=45)
    last_name: constr(max_length=45)
    last_update: datetime

    class Config:
        orm_mode = True

class Category(BaseModel):
    category_id: int
    name: constr(max_length=25)
    last_update: datetime

class Country(BaseModel):
    country_id: int
    country: constr(max_length=50)
    last_update: datetime

class Language(BaseModel):
    language_id: int
    name: constr(max_length=20)
    last_update: datetime

class City(BaseModel):
    city_id: int
    city: str
    country_id: int
    last_update: datetime
    country: List[Country]

class RatingEnum(str, Enum):
    G = 'G'
    PG = 'PG'
    PG_13 = 'PG-13'
    R = 'R'
    NC_17 = 'NC-17'

class TsVector(UserDefinedType):
    "Holds a TsVector column"

    name = "TSVECTOR"

    def get_col_spec(self):
        return self.name

class Film(BaseModel):
    film_id: int
    title: str
    description: str
    release_year: int 
    language_id: int
    rental_duration: int
    rental_rate: float
    length: int
    replacement_cost: float
    rating: RatingEnum = RatingEnum.G
    last_update: datetime
    special_features: List[str]
    #fulltext: TsVector
    language: List[Language]

    # class config:
    #     arbitrary_types_allowed = True

class Addres(BaseModel):
    address_id: int
    address: constr(max_length=50)
    address2: constr(max_length=50)
    district: constr(max_length=20)
    city_id: int
    postal_code: constr(max_length=10)
    phone: constr(max_length=20)
    last_update: datetime
    city: List[City]

class FilmActor(BaseModel):
    actor_id: int
    film_id: int
    last_update: datetime
    actor: List[Actor]
    film: List[Film]

class FilmCategory(BaseModel):
    film_id: int
    category_id: int
    last_update: datetime
    category: List[Category]
    film: List[Film]

class Inventory(BaseModel):
    inventory_id: int
    film_id: int
    store_id: int
    last_update: datetime
    film: List[Film]

class Customer(BaseModel):
    customer_id: int
    store_id: int
    first_name: constr(max_length=45)
    last_name: constr(max_length=45)
    email: constr(max_length=50)
    address_id: int
    activebool: bool
    create_date: date
    last_update: datetime
    active: int
    address: List[Addres]

class Staff(BaseModel):
    staff_id: int
    first_name: constr(max_length=45)
    last_name: constr(max_length=45)
    address_id: int
    email: constr(max_length=50)
    store_id: int
    active: bool
    username: constr(max_length=16)
    password: constr(max_length=40)
    last_update: datetime
    #picture = Column(LargeBinary)
    address: List[Addres]

class Rental(BaseModel):
    rental_id: int
    rental_date: datetime
    inventory_id: int
    customer_id: int
    return_date: datetime
    staff_id: int
    last_update: datetime
    customer: List[Customer]
    inventory: List[Inventory]
    staff: List[Staff]

class Store(BaseModel):
    store_id: int
    manager_staff_id: int
    address_id: int
    last_update: datetime
    address: List[Addres]
    manager_staff: List[Staff]

class Payment(BaseModel):
    payment_id: int
    customer_id: int
    staff_id: int
    rental_id: int
    amount: float
    payment_date: datetime
    customer: List[Customer]
    rental: List[Rental]
    staff: List[Staff]