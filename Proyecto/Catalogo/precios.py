from calculador_precios import *

print("APP PARA CALCULAR GASTOS DE ELABORACION DE RECETAS")

nombre = input("Ingresa tu nombre: ")
receta = input(f"Hola, {nombre}, cuéntame qué receta deseas preparar: ")
cantidad = int(input(f"¿Qué cantidad de {receta}(s) deseas preparar? "))

while True:
    try:
        num_ingredientes = int(input("Ingrese la cantidad de ingredientes a usar: "))
        ingredientes = Ingrediente.crear_ingredientes(num_ingredientes)
        break
    except ValueError:
        print("Debe ingresar números enteros")

for ingrediente in ingredientes:
    print(ingrediente.costo())

costo_total = sum(ingrediente.costo() for ingrediente in ingredientes)
print(f"{nombre}, el gasto total para preparar {cantidad} de {receta} es {costo_total}. Así que cada unidad tiene un costo de {costo_total/cantidad}.")
