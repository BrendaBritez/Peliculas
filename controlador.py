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