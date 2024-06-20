import pyodbc
from workdates import convertstr

isthere=False

class DbAcess:
    
    def __init__(self,RouteDB):
        self.RouteDB = RouteDB
        self.conn_str = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            f'DBQ={self.RouteDB};'
        )
        self.conn = pyodbc.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        self.NmDB = ""
        self.CAMP = ""
    
    def Getids(self):
        sql_query = f"SELECT {'id'} FROM {self.NmDB}"
        self.cursor.execute(sql_query)
        ids = [row[0] for row in self.cursor.fetchall()]
        return ids

    def modify(self,Nmdb,CAMP):   
            self.NmDB = Nmdb
            self.CAMP = CAMP

  
    def closeDB(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def insertdate(self,dates,flags=False):
        self.cursor.execute(f"SELECT {self.CAMP} FROM {self.NmDB}")
        valores = self.cursor.fetchall()

        datos_a_insertar= convertstr(dates)
        if flags == False:
            for dato in datos_a_insertar:
                self.cursor.execute(f"INSERT INTO {self.NmDB} ({self.CAMP}) VALUES (?)", dato)
            self.closeDB()
        else:     
            condicion_actualizar = f"{self.CAMP} = '' OR Nombre IS NULL"
            sql_update = f"UPDATE {self.NmDB} SET {self.CAMP} = ? WHERE {condicion_actualizar}"

            for dato in datos_a_insertar:
                for valor in valores:
                    if valor == "":
                        print(dato)
                        self.cursor.execute(sql_update, dato)
                    
            self.closeDB()
        
        

    def deleteALL(self):
        sql_query = f"SELECT {'id'} FROM {self.NmDB}"
        self.cursor.execute(sql_query)
        ids = [row[0] for row in self.cursor.fetchall()]
        for id in ids:
            sql_query = f"DELETE FROM {self.NmDB} WHERE ID = ?"  
            self.cursor.execute(sql_query, id)
        self.closeDB()
        

#db = DbAcess("C:/Users/MINEDUCYT/Documents/Actividad4.accdb")
#db.modify("Empleados")

#db.deleteALL()