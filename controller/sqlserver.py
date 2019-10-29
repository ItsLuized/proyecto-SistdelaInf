import pyodbc

class SQLServerController():

    def __init__(self):
        #Iniciar conexión

        #Cadena de conexión 
        self.conn = pyodbc.connect("Driver = {ODBC Driver 17 for SQL Server};" 
                                "Server = LAPTOP-24PFM6VE;" #Nombre del servidor SQL Server 
                                "Database = db_name;" #Nombre de la DB
                                "Trusted_Connection = yes;") #Que Windows, o el OS, haga la autentificación


    def insert(self, sql, val):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql, val)
            self.conn.commit()
        except pyodbc.IntegrityError as e:
            print("Error: Error insertando datos: \t", e)

    def select(self, sql, val):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql, val)
                cursor.close()
                result = cursor.fetchall()

                return result

        except pyodbc.IntegrityError as e:
            print("Error: Error realizando un query: \t", e)
    