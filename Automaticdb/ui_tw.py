import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import DBacess


datetxt = ""

#base de datos var
db=""


    
def insertdt(NTB,CM):
    global datetxt
    global db
    db.modify(NTB,CM)
    db.insertdate(datetxt,False)
    print("la operacion se realizo exitosamente")

def obtener_texto(GETdt,NTB,CM):
    global datetxt
    datetxt = GETdt.get("1.0", tk.END).strip()
    messagebox.showinfo("Texto Ingresado", f"Texto: {datetxt}")
    insertdt(NTB=NTB.get(),CM=CM.get())
   


def main():
    ventana = tk.Tk()
    ventana.title("Ingreso de Texto")

    #ingresar datos para la base   
    Nametb = tk.Entry(ventana, width=40)
    Nametb.pack(padx=20, pady=20)

    Camptb = tk.Entry(ventana, width=40)
    Camptb.pack(padx=20, pady=20)
    
    text = tk.Text(ventana, height=5, width=40)
    text.pack(pady=20)


    boton_obtener = tk.Button(ventana, text="Obtener Texto", command=lambda: obtener_texto(text,Nametb,Camptb))
    boton_obtener.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    
    def Get_db(): 

        global db 
        archivo = filedialog.askopenfilename()
        ruta_DB.set(archivo)
        print(archivo)
        db = DBacess.DbAcess(archivo)
        ventana.destroy()
       
    
    ventana = tk.Tk()
    ventana.title("Archivo Acess")

    ruta_DB = tk.StringVar()

    etiqueta_ruta = tk.Label(ventana, textvariable=ruta_DB)
    etiqueta_ruta.pack()

    boton_seleccionar = tk.Button(ventana, text="Seleccionar Archivo", command=Get_db)
    boton_seleccionar.pack()
    
    
    ventana.mainloop()
    

    main()