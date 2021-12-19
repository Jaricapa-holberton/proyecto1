#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI, Body, Query, Path

app = FastAPI()

#Models
class Person(BaseModel):              #Se crea una clase que herede la clase BaseModel, los atributos de la clase serían los atributos de la entidad/modelo
    first_name: str 
    last_name: str
    age: int                          #Se usan los dos puntos y el tipo de dato para definir que tipo de dato va a llevar este atributo en JSON
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None #Para poder tener atributos opcionales con un tipo de dato, se usa la clase Optional[{type}] y se pone un valor por defecto que                                           sería None, que en bases de datos es null


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