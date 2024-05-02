import tkinter as tk

def registrar_datos():
    nombre = cnombre.get()
    apellido = capellido.get()
    edad = cedad.get()
    sexo = opcion.get()  
    ciudad = Cciudad.get(Cciudad.curselection())

    tk.Label(Marco, text="Nombre: "+ nombre).pack()
    tk.Label(Marco, text="Apellido: "+ apellido).pack()
    tk.Label(Marco, text="Edad: "+ edad).pack()
    tk.Label(Marco, text="Sexo: "+ sexo).pack() 
    tk.Label(Marco, text="Ciudad: "+ ciudad).pack()

ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("1024x960")

lnombre = tk.Label(ventana, text="Nombre:")
lnombre.grid(row=0, column=0)
cnombre = tk.Entry(ventana, width=30)
cnombre.grid(row=0, column=1)

lapellido = tk.Label(ventana, text="Apellido:")
lapellido.grid(row=1, column=0)
capellido = tk.Entry(ventana, width=30)
capellido.grid(row=1, column=1)

ledad = tk.Label(ventana, text="Edad:")
ledad.grid(row=2, column=0)
cedad = tk.Entry(ventana, width=30)
cedad.grid(row=2, column=1)

lsexo = tk.Label(ventana, text="Sexo:")
lsexo.grid(row=3, column=0)


opcion = tk.StringVar()

sexoS = tk.Radiobutton(ventana, text="Masculino", variable=opcion, value="Masculino")
sexoS.grid(row=3, column=1)

sexoS = tk.Radiobutton(ventana, text="Femenino", variable=opcion, value="Femenino")
sexoS.grid(row=3, column=2)

lciudad = tk.Label(ventana, text="Ciudad")
lciudad.grid(row=4, column=0)

Cciudad = tk.Listbox(ventana, width=15)
elementos = ["Cartagena", "Bogotá", "Medellín"]
for elemento in elementos:
    Cciudad.insert(tk.END, elemento)
Cciudad.grid(row=4, column=1)

boton = tk.Button(ventana, text='Registrar', command=registrar_datos)
boton.grid(row=5, column=1)

Marco = tk.Frame(ventana, width=200, height=100, bd=2, relief="raised")
Marco.grid(row=6, column=0)

ventana.mainloop()