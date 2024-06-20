import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import index 


datetxt = ""



def Get_db():
    archivo = filedialog.askopenfilename()
    ruta_DB.set(archivo)
   

    
def insertdt():
    global datetxt
    conn, cr = index.opendb()
    index.insertdate("Empleados","Nombre",datetxt,cr=cr)
    index.closeDB(conn=conn,cursor=cr)
    print("la operacion se realizo exitosamente")

def obtener_texto():
    global datetxt
    datetxt = entrada_texto.get()
    messagebox.showinfo("Texto Ingresado", f"Texto: {datetxt}")
    insertdt()




ventana = tk.Tk()
ventana.title("Ingreso de Texto")


#seleccion la base de datos el archivo
ruta_DB = tk.StringVar()

etiqueta_ruta = tk.Label(ventana, textvariable=ruta_DB)
etiqueta_ruta.pack()

boton_seleccionar = tk.Button(ventana, text="Seleccionar Archivo", command=Get_db)
boton_seleccionar.pack()

#ingresar datos para la base
entrada_texto = tk.Entry(ventana, width=40)
entrada_texto.pack(padx=20, pady=20)


boton_obtener = tk.Button(ventana, text="Obtener Texto", command=obtener_texto)
boton_obtener.pack(pady=10)


ventana.mainloop()



#conn, cr = index.opendb()
#index.GetAll("Empleados",cr=cr)
#ndex.deletALL("Empleados",cr=cr)
#index.closeDB(conn=conn,cursor=cr)

