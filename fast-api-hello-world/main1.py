#Python
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel, Field

#FastAPI
from fastapi import FastAPI, Body, Query, Path

app = FastAPI()

#Models

class Location(BaseModel):
    city: str 
    state: str
    country: str
    
class HairColor(Enum):
    white = 'white'
    black = 'black'
    brown = 'brown'
    blonde = 'blonde'

class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    age: int = Field(
        ...,
        gt=0,
        le=130
    )
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)  

@app.get("/")                         #Un path operation que usa el método get en la ruta /
def home():
    return {"Hello": "World"}

@app.post("/person/new")              #Un path operation que usa el metodo post en la ruta /person/new
def create_person(person: Person = Body(...)):  #Se usa un Request Body, se importa la clase Body de FastAPI esta en su constructor usa un parametro, en este caso son                                                    los 3 puntos, que indican que ese Request Body es obligatorio. Se usa una variable que serviría como parametro para                                                      usar el modelo, en este caso person que sería tipo Person
    return person

# Validations: Query Parameters

@app.get('/person/detail')
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=30,
        regex='^[A-Za-z]*$',
        title="Person Name",
        description="This is the person name. It's between 1 and 30 characters"
    ),
    age: int = Query(
        ...,
        title="Person Age",
        description="This is the person age. It's required"
    )
):
    return {name: age}


# Validations: Path Parameters

@app.get('/person/detail/{person_id}')
def show_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID. It's required",
        gt=0
    )
):
    return {person_id: "It exists!"}

# Validations: Request Body
@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt=0
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    result = dict(person)
    result.update(dict(location))

    return result