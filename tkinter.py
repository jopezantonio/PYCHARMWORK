import tkinter

ventana = tkinter.Tk()
ventana.configure(bg="#000000")
titulo = tkinter.Label(ventana, text="Hola mundo", font=("Arial", 18), padx=20, pady = 40, bg="#000000", fg="#00ff00")

titulo.pack()

ventana.mainloop()