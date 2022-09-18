#para listar las librerias que se estan usando : pip freeze > requeriments.txt
#uvicorn app:app --reload cada que se guarda va recargar 

from fastapi import FastAPI, Path, Body
from bd import BD
from controlador import MoviesController
from models import Movies
#el fat api sirve para crear un server
#creo un objeto de tipo fastapi que es el que va levantar el server
#cuando el servidor arranque inicia y cuando se apaga pues aha
app: FastAPI = FastAPI()
@app.on_event("startup")
def conectar():
    BD.conectar()

@app.on_event("shutdown")
def desconectar():
    BD.desconectar()

#crear rutas para consultar todas las peliculas
#la barra hace referencia a la url 
@app.get(
    path='/movies',
    tags=["Movies"],
    summary="listar todas las peliculas",
    response_model=list[Movies]
)
def getMovie()-> list[Movies]:
    datos=MoviesController.getMovies()
    return datos[1]

#rut Para eliminar
@app.delete(
    path='/movies/{id_audiovisual}',
    tags=["Movies"],
    summary="Eliminar peliculas",
    response_model=str
)
def deleteMovies(id_audiovisual:int=Path(...))->str:
    respuesta=MoviesController.deleteMovies(id_audiovisual)
    return respuesta[1]

#para actualizar una pelicula
@app.put(
    path='/movies',
    tags=["Movies"],
    summary="Poner peliculas",
    response_model=str
)
def putMovie(argumento:Movies=Body(...))->str:
    respuesta=MoviesController.updateMovies(argumento)
    return respuesta[1]

#para crear una pelicula nueva o añadir
@app.post(
    path='/movies',
    tags=["Movies"],
    summary="Publicar peliculas",
    response_model=str
)
def postinsertarMovie(argumento:Movies=Body(...))-> str:
    respuesta=MoviesController.insertMovie(argumento)
    return respuesta[1]

#------------------------------------------------------------
#le añadis un parametro en la ruta pero no sabes que clase es y le pones un nombre generico para usar dp

@app.get(
    path='/movies/{id}',
    tags=["Movies"],
    summary="listar todas las peliculas",
    response_model=Movies
)
#el nuevo parametro que vos estas esperando le pones en tu funcion y definis el tipo 
#hay que cambiar el coso que retorna pq lo que hay dentro del id es un diccionario 
#path path signidica que el parametro que estoy pidiendo es obligatorio

def getOneMovie(id:int=Path(...))-> Movies: #Esta funcion retorna un objeto del tipo pelicula
    respuesta=MoviesController.getOneMovie(id)
    return respuesta[1]






