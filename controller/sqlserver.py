import pyodbc

class SQLServerController():

    def __init__(self):
        #Iniciar conexión

        #Cadena de conexión 
        self.conn = pyodbc.connect(driver='{SQL Server}', host='LAPTOP-24PFM6VE', database='Test',
                      trusted_connection='yes')
        
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
                result = cursor.fetchall()

                return result

        except pyodbc.IntegrityError as e:
            print("Error: Error realizando un query: \t", e)
    

    def selectn(self, sql):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()

                return result

        except pyodbc.IntegrityError as e:
            print("Error: Error realizando un query: \t", e)