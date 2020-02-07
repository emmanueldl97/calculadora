from tkinter import *
ventana=Tk()
ventana.config(bg="purple")

miframe=Frame(ventana, width=300, height=300)
miframe.config(bg="gray")
miframe.pack()

#=============LABEL===========
nombre=Label(miframe, text="nombre")
nombre.grid(row=0, column=0, pady=10, padx=10)
apellido=Label(miframe, text="apellido")
apellido.grid(row=1, column=0, pady=10, padx=10)
telefono=Label(miframe, text="telefono")
telefono.grid(row=2, column=0, pady=10, padx=10)

#==============ENTRY===============
entrynombre=Entry(miframe)
entrynombre.grid(row=0, column=1, pady=10, padx=10)
entryapellido=Entry(miframe)
entryapellido.grid(row=1, column=1, pady=10, padx=10)
entrytelefono=Entry(miframe)
entrytelefono.grid(row=2, column=1, pady=10, padx=10)

#=============BOTONES===========
aceptar=Button(miframe, text="aceptar")
aceptar.grid(row=4, column=0, pady=15, padx=10 )
aceptar.config(bg="yellow")
cancelar=Button(miframe, text="cancelar")
cancelar.grid(row=4, column=1, pady=15, padx=10)
cancelar.config(bg="green")





ventana.mainloop()