#Solamente esta aca para conectarse a la base de datos
import psycopg2 
from psycopg2.extensions import connection, cursor

class BD:
    conexion:connection=None
    dbcursor:cursor=None
    
    @staticmethod 
    def conectar():
        try:
            BD.conexion=psycopg2.connect(f"dbname=AdministradorPeliculas user=postgres port=5432 host=localhost password=brenda1997")
            BD.dbcursor=BD.conexion.cursor()
        except Exception as er:
            print(er)
 
    @staticmethod 
    def desconectar():
        try:
            BD.conexion.close()
            BD.dbcursor.close()
        except Exception as er:
            print(er)
            