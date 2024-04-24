import tkinter as tk


def mifuncion():
    print("Este mensaje es del boton")


def mifuncion2():
    print("Este mensaje es del otro boton")


vent = tk.Tk()
vent.title("APP DE SUMA")
vent.geometry("400x200")
vent.config(bg="#CC99FF")

lbl = tk.Label(vent, bg="#CC99FF", text="ESTE ES UN LABEL")
lbl.pack()
lbl["bg"] = "green"
lbl["fg"] = "white"
vent.iconbitmap("movies.ico")

btn = tk.Button(vent, text="Presionar", command=mifuncion)
btn.config(fg="red", bg="yellow")  # dos maneras distintas de configurar una es esta con config
btn["bg"] = "blue"  # La otra manera es esta semejante a diccionarios.
btn["fg"] = "white"
btn.pack()

btn1 = tk.Button(vent, text="Otro boton", command=mifuncion2)
btn1.place(relx=0.6, rely=0.1)
btn1.pack()

vent.mainloop()
