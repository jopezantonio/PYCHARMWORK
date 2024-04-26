class Precios:
    receta = ""

    @staticmethod
    def obtener_receta():
        receta = input("Hola, ingrese qué receta desea preparar: ")
        Precios.receta = receta


class Ingrediente:
    costo_total = 0

    def __init__(self, nombre, producto, precio, medida, cantidad_kg, cantidad_usada):
        self.nombre = nombre
        self.producto = producto
        self.precio = precio
        self.medida = medida
        self.cantidad_kg = cantidad_kg
        self.cantidad_usada = cantidad_usada

    @staticmethod
    def crear_ingredientes(num_ingredientes):
        ingredientes = []
        for i in range(1, num_ingredientes + 1):
            nombre = f"Ingrediente_{i}"
            producto = input(f"Identifique cuál es el ingrediente {i}: ")
            precio = float(input(f"Ingrese el precio de {producto}: "))
            medida = input(f"Ingrese la medida de {producto} (kilo/maple/unidad): ").lower()
            cantidad_kg = 0
            if medida == "kilo":
                cantidad_kg = float(input(f"Ingrese la cantidad de kilos del paquete o saco de {producto}: "))
            cantidad_usada = float(input(f"Ingrese la cantidad usada de {producto}: "))
            ingrediente = Ingrediente(nombre, producto, precio, medida, cantidad_kg, cantidad_usada)
            ingredientes.append(ingrediente)
        return ingredientes

    def costo(self):
        try:
            if self.medida == "kilo":
                peso_gramos = self.cantidad_kg * 1000
                porcentaje_ingrediente_usado = self.cantidad_usada / peso_gramos
            elif self.medida == "maple":
                porcentaje_ingrediente_usado = self.cantidad_usada / 30
            elif self.medida == "unidad":
                porcentaje_ingrediente_usado = self.cantidad_usada
            else:
                raise ValueError("La medida ingresada no es válida.")

            costo_ingr = self.precio * porcentaje_ingrediente_usado
            Ingrediente.costo_total += costo_ingr
            print(f"El costo de {self.producto} es {costo_ingr}")
            print(f"El total gastado en la preparación de {Precios.receta} es {Ingrediente.costo_total}")
        except ZeroDivisionError:
            return 0  # Maneja el caso de división por cero devolviendo un valor numérico apropiado
        except ValueError as e:
            return 0  # Maneja otros errores devolviendo un valor numérico apropiado


print("APP PARA CALCULAR GASTOS DE ELABORACIÓN DE RECETAS")

nombre = input("Ingresa tu nombre: ")
Precios.obtener_receta()
cantidad = int(input(f"¿Qué cantidad de {Precios.receta}(s) deseas preparar?: "))

while True:
    try:
        num_ingredientes = int(input("Ingrese la cantidad de ingredientes a usar: "))
        ingredientes = Ingrediente.crear_ingredientes(num_ingredientes)
        break
    except ValueError:
        print("Debe ingresar números enteros")

for ingrediente in ingredientes:
    ingrediente.costo()
