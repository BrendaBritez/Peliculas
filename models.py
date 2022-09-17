#
from pydantic import BaseModel, Field #esta field sive para validar un campo
#greter o sea mayor que o igual a 1 
class Movies(BaseModel):
    id_audiovisual:int=Field(ge=1)
    titulo:str=Field(...) #usa puntos dentro para decir que es un campo obligatorio de completar
    descripcion:str=Field(...)
    genero:str=Field(...)
    anho_lanzamiento:int=Field(...)
    clasificacion:str=Field(...)
    tipo:str=Field(...)
    class Config:
        #es una carga de ejemplo
        schema_extra={
            "example":{
                "id_audiovisual":1,
                "titulo":"titanic",
                "descripcion":"Esta pelicula trata sobre el naufragio del barco que lleva el nombre de la pelicula, entrelazando la historia de amor de dos jovenes",
                "genero":"Drama",
                "anho_lanzamiento":1997,
                "clasificacion":"B",
                "tipo":"Pelicula"
            }
        }
    @staticmethod
    def getMovies()->str:
        return "select * from audiovisual"
