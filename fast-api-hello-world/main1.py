#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI, Body, Query

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

# Validaciones.
@app.get("/person/detail") # Ruta para realizar la consulta.
def show_person(
	#Opcional.
	name: Optional[str] = Query(None, min_length=1, max_length=50),
	# Obligatorio.
	age: int = Query(...)
   ):

   return {name: age}