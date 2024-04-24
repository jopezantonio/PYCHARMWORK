from tkinter import  Frame, Label, Entry, Button, END

class Fsuma(Frame):
    def __init__(self, vent=None):
        super().__init__(vent, width=480, height=320)
        self.vent = vent
        self.pack()
        self.create_widgets()

    def suma(self):
        n1 = self.txt1.get()
        n2 = self.txt2.get()
        res = float(n1) + float(n2)
        self.txt3.delete(0, END)
        self.txt3.insert(0, res)
        self.txt1.delete(0, END)
        self.txt2.delete(0, END)

    def create_widgets(self):
        self.lbl1 = Label(self, text="Primer numero", bg="yellow")
        self.lbl1.place(x=10, y=10, width=100, height=30)
        self.txt1 = Entry(self, bg="pink")
        self.txt1.place(x=150, y=10, width=100, height=30)

        self.lbl2 = Label(self, text="Segundo numero", bg="#7DCEA0")
        self.lbl2.place(x=10, y=50, width=100, height=30)
        self.txt2 = Entry(self, bg="pink")
        self.txt2.place(x=150, y=50, width=100, height=30)

        self.btn = Button(self, text="Sumar", command=self.suma)
        self.btn.place(x=280, y=50, width=80, height=30)

        self.lbl3 = Label(self, text="Resultado", bg="#E74C3C")
        self.lbl3.place(x=10, y=120, width=100, height=30)
        self.txt3 = Entry(self, bg="pink")
        self.txt3.place(x=150, y=120, width=100, height=30)

