from tkinter import Tk
from client.clase_suma import Fsuma


def main():
    vent = Tk()
    vent.title("Aplicacion para sumar")
    app = Fsuma(vent=vent)
    app.mainloop()

if __name__ == "__main__":
    main()
