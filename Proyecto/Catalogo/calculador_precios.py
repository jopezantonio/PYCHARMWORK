class Ingrediente():
    costo_total = 0

    def __init__(self, nombre, producto, precio, medida, cantidad_usada):
        self.nombre = nombre
        self.producto = producto
        self.precio = precio
        self.medida = medida
        self.cantidad_usada = cantidad_usada




    @staticmethod
    def crear_ingredientes(num_ingredientes):
        ingredientes = []
        for i in range(1, num_ingredientes + 1):
            nombre = f"Ingrediente_{i}"
            producto = input(f"Identifique cual es el ingrediente{i}: ")
            precio = float(input(f"Ingrese precio de {producto}: "))
            medida = input(f"Ingrese medida de {producto} kilo/saco/maple: ").lower()
            cantidad_usada = float(input(f"Ingrese cantidad usada de {producto}: "))
            ingrediente = Ingrediente(nombre, producto, precio, medida, cantidad_usada)
            ingredientes.append(ingrediente)
        return ingredientes


    def costo(self):
        try:
            if self.medida == "kilo":
                cantidad_para_kg = self.cantidad_usada / 1000
                costo_ingr = self.precio * cantidad_para_kg
                Ingrediente.costo_total += costo_ingr
                print(f"El costo de {self.producto} es {costo_ingr}")
                return costo_ingr
            if self.medida == "saco":
                cantidad_para_kg = self.cantidad_usada / 20000
                costo_ingr = self.precio * cantidad_para_kg
                Ingrediente.costo_total += costo_ingr
                print(f"El costo de {self.producto} es {costo_ingr}")
                return costo_ingr
            if self.medida == "maple":
                costo_unidad = self.precio / 30
                costo_ingr = costo_unidad * self.cantidad_usada
                Ingrediente.costo_total += costo_ingr
                print(f"El costo de {self.producto} es {costo_ingr}")
                return costo_ingr
            else:
                raise ValueError("La medida ingresada no es válida.")
        except ZeroDivisionError:
            return 0  # Maneja el caso de división por cero devolviendo un valor numérico apropiado
        except ValueError as e:
            return 0  # Maneja otros errores devolviendo un valor numérico apropiado



