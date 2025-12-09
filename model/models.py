from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import date

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    published_year: int
    isbn: str

class Students(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    faculty: str
    dob: date
    address: str
    contact_number: int = Field(
        ge=1000000, 
        le=999999999999999,
        description="Phone number (7-15 digits)"
    )
