import tkinter as tk

def barra_menu(root):
    barra_menu= tk.Menu(root)
    root.config(menu = barra_menu, width = 300, height = 300)

    # Menú de Inicio
    menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = "Inicio", menu = menu_inicio)

    menu_inicio.add_command(label = "Crear Registro en DB")
    menu_inicio.add_command(label="Eliminar Registro en DB")
    menu_inicio.add_command(label="Salir", command = root.destroy)

    # Menú de Edición
    menu_editar = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Editar", menu=menu_editar)
    menu_editar.add_command(label="Editar Película")
    menu_editar.add_command(label="Editar Autor")

    # Menú de Configuración
    menu_configurar = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Configurar", menu=menu_configurar)
    menu_configurar.add_command(label="Editar Nombre")
    menu_configurar.add_command(label="Editar Título")

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width = 480, height = 320 )
        self.root = root
        self.pack()
        self.config(bg='#5dade2')