from calculador_precios import *

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