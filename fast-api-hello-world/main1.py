# Python
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel, Field, EmailStr

# FastAPI
from fastapi import FastAPI, Body, Query, Path, Form, status, Header, Cookie, UploadFile, File, HTTPException

app = FastAPI()

class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"


class Location(BaseModel):
    city: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="The city where the person lives",
        example="New York",
    )
    state: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="The state where the person lives",
        example="New York",
    )
    country: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="The country where the person lives",
        example="United States",
    )

class PersonBase(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example='Marty'
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example='McFly'
        )
    age: int = Field(
        ...,
        gt=0,
        le=115,
        example='20'
        )
    hair_color: Optional[HairColor] = Field(default=None, example='black')
    is_married: Optional[bool] = Field(default=None, example='False')


class Person(PersonBase):
    password: str = Field(
        ...,
        min_length=8
        )

class PersonOut(PersonBase):
    pass


class LoginOut(BaseModel):
    username: str = Field(..., max_length=40, example="miguel1221")
    message: str = Field(default="Login Succesfully!")


@app.get(path="/", status_code=status.HTTP_200_OK, tags=["Home"], summary="Display the home page")
def home():
    """
    # Home

    This path operation display the home page

    ### Parameters
    - None

    ### Returns
    A dictionary with a gretting
    """
    return {"Hello": "World!"}

# Request and Response Body

@app.post(path='/person/new', response_model=PersonOut, status_code=status.HTTP_201_CREATED, tags=["Person"], summary="Create a new person")
def create_person(person: Person = Body(...)):
    """
    # Create Person

    This path operation creates a person in the app and save the information in the database

    ### Parameters
    - Request body parameter: 
        - **person: Person** -> A person model with first name, last name, age, hair color and marital stauts

    ### Returns
    A person model with first name, last name, age, hair color and marital status
    """
    return person


# Validaciones: Query Parameters

@app.get(path="/person/detail", status_code=status.HTTP_200_OK, tags=["Person"], summary="Display all the persons in the database")
def show_person(
    name: Optional[str] = Query(
        None, min_length=1,
        max_length=50,
        title="Person Name",
        description="This is the person name,  It's between 1 and 50 characters",
        example="Rocio"
        ),
    age: str = Query(
        ...,
        title="Person Age",
        description="This is the person age, It's required",
        example="25"
        )
):
    return {name: age}

# Validaciones Path Paremeters
persons = [1, 2, 3, 4, 5, 123]

@app.get(
    path='/person/detail/{person_id}',
    status_code=status.HTTP_200_OK,
    tags=["Person"],
    summary="Display a person by id"
)
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title='Person Id',
        description='Person ID on the Database',
        example=20
    )
):

    if person_id not in persons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Person not found'
        )

    return {person_id: 'it exists!'}

# Validaciones: Request Body


@app.put(path="/person/{person_id}", status_code=status.HTTP_202_ACCEPTED, tags=["Person"], summary="Update the data of a person")
def update_person(
    person_id: int = Path(
        ...,
        title='Person ID',
        description='This is the person ID. It is required',
        gt=0,
        example=32
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results


# Forms
@app.post(path="/login/", response_model=LoginOut, status_code=status.HTTP_202_ACCEPTED, tags=["Login"], summary="Login a user person")
async def login(username: str = Form(...), password: str = Form(...)):
    return LoginOut(username=username)


@app.post(
    path='/contact',
    status_code=status.HTTP_200_OK,
    tags=["Contact"],
    summary="Create a new contact"
)
def contact(
    first_name: str = Form(
        ...,
        max_length=50,
        min_length=1,
        example='Peter'
    ),
    last_name: str = Form(
        ...,
        max_length=20,
        min_length=1,
        example='Chiguire'
    ),
    email: EmailStr = Form(
        ...,
        example='peterchiguire@gmail.com'
    ),
    message: str = Form(
        ...,
        min_length=1,
        max_length=280,
        example='Hola, estoy interesado en tu proyecto, jajaj xdddd'
    ),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)
):
    return {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'message': message,
        'user_agent': user_agent,
        'ads': ads
    }


@app.post(path='/post-image', status_code=status.HTTP_200_OK, tags=["Files"], summary="Create a new image post")
def post_image(
    image: UploadFile = File(...)
):
    return {
        'filename': image.filename,
        'format': image.content_type,
        'size(kb)': round(len(image.file.read()) / 1024, 2)
    }

