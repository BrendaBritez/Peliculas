#Se consulta a labase de datos y se crean los modelos con esos datos retornados
#Se manipula la base de datos con los datos que nos llegan 

from bd import BD
from models import Movies

class MoviesController:
    @staticmethod
    def getMovies()->tuple:
        BD.dbcursor.execute(Movies.getMovies())
        datos=BD.dbcursor.fetchall()
        listaPeliculas:list[Movies]=[]
        for dato in datos:
            variablePelicula:Movies=Movies(
                id_audiovisual=dato[0],
                titulo=dato [1],
                descripcion=dato[2],
                genero=dato[3],
                anho_lanzamiento=dato[4],
                clasificacion=dato[5],
                tipo=dato[6]
            )
            listaPeliculas.append(variablePelicula)
        return (1,listaPeliculas)
    
    @staticmethod
    def getOneMovie(id_audiovisual:int)->tuple:
        BD.dbcursor.execute(Movies.getOneMovie(),(id_audiovisual,))
        dato=BD.dbcursor.fetchone()
        variablePelicula:Movies=Movies(
                id_audiovisual=dato[0],
                titulo=dato [1],
                descripcion=dato[2],
                genero=dato[3],
                anho_lanzamiento=dato[4],
                clasificacion=dato[5],
                tipo=dato[6]
        )
        return (1,variablePelicula)
    @staticmethod
    def insertMovie(argumento:Movies)->tuple:
        BD.dbcursor.execute(Movies.insertMovies(),(argumento.titulo,argumento.descripcion,argumento.genero,argumento.anho_lanzamiento,argumento.clasificacion,argumento.tipo))
        BD.conexion.commit()
        return (1, "Creado")

    @staticmethod
    def updateMovies(argumento:Movies)->tuple:
        BD.dbcursor.execute(Movies.updateMovies(),(argumento.titulo,argumento.descripcion,argumento.genero,argumento.anho_lanzamiento,argumento.clasificacion,argumento.tipo, argumento.id_audiovisual))
        BD.conexion.commit()
        return (1, "Actualizado")      

    @staticmethod
    def deleteMovies(id_audiovisual:int)->tuple:
        BD.dbcursor.execute(Movies.deleteMovies(),(id_audiovisual,))
        BD.conexion.commit()
        return (1,"eliminado")
        
