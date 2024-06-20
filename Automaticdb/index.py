import pyodbc
from workdates import convertstr

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\MINEDUCYT\Documents\Actividad4.accdb;'
)



def opendb():
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    return conn, cursor

# Funciones y cierre de la base de datos
def insertdate(NmDB,CAMP,dates,cr):
    datos_a_insertar= convertstr(dates)
    for dato in datos_a_insertar:
        cr.execute("INSERT INTO "+NmDB+" ("+CAMP+") VALUES (?)", dato)

def deletALL(NmDB,cr):
    sql_query = f"SELECT {'id'} FROM {NmDB}"
    cr.execute(sql_query)
    ids = [row[0] for row in cr.fetchall()]
    for id in ids:
        sql_query = f"DELETE FROM {NmDB} WHERE ID = ?"  
        cr.execute(sql_query, id)


def GetAll(NmBD,cr):
    cr.execute("SELECT * FROM "+NmBD)
    for row in cr.fetchall():
        print(row)


def closeDB(conn,cursor):
    conn.commit()
    cursor.close()
    conn.close()



