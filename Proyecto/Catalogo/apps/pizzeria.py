import tkinter as tk

def pedido():
    opcion = txt1.get()
    if opcion >= "1" and opcion <= "2":
        if opcion == "1":
           mnsj1 = "USTED ORDENO UNA PIZZA XXL"
           lbl5= tk.Label(ventana, text=mnsj1)
           lbl5.place(x=130, y=280)
           txt5.insert(0, lbl5)
        else:
            pass





ventana = tk.Tk()
ventana.title("PIZZERIA BELLA NAPOLI")
ventana.config(width=480, height=500, bg="#acd9e2")
ventana.resizable(0, 0)

lbl1 = tk.Label(ventana, text="MENU DE PIZZAS")
lbl1.place(x=190, y=20)
lbl1.config(bg="blue", fg="white")

lbl2 = tk.Label(ventana, text="Opcion 1. Pizza Vegetariana")
lbl2.place(x=45, y=80)

lbl3 = tk.Label(ventana, text="Opcion 2. Pizza Peperonni")
lbl3.place(x=45, y=120)

lbl4 = tk.Label(ventana, text="Por favor seleccione una opción:")
lbl4.place(x=150, y=180)

txt1 = tk.Entry(ventana,)
txt1.config(width=4)
txt1.place(x=220, y=210)

btn1 = tk.Button(text="GENERAR PEDIDO", command=pedido)
btn1.place(x=180, y=240)




ventana.mainloop()





print("Opcion 1. Pizza Vegetariana", "\n" * 2)
print("Opcion 2. Pizza No Vegetariana", "\n" * 2)

pizza = int(input("///////Ingrese el numero de opcion deseado y presione enter: "))
print("\n")
print("\n")
print("\n")
print("\n")
base = ["tomate", "mozzarella"]




