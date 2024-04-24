"""
Listas
Python tiene varios tipos de datos compuestos, usados para agrupar otros valores. El más versátil es la lista, la cual puede
ser escrita como una lista de valores separados por coma (ítems) entre corchetes. Las listas pueden contener ítems de
diferentes tipos, pero usualmente los ítems son del mismo tipo:"""
cuadrados = [1, 4, 9, 16, 25]
print(cuadrados) # [1, 4, 9, 16, 25]

#Como las cadenas de caracteres (y todos los otros tipos sequence integrados), las listas pueden ser indexadas y rebanadas:
print(cuadrados[0]) # índices retornan un ítem   1

print(cuadrados[-1]) # 25

print(cuadrados[-3:]) # rebanadas retornan una nueva lista  [9, 16, 25]

"""Todas las operaciones de rebanado devuelven una nueva lista conteniendo los elementos pedidos. Esto significa que la
siguiente rebanada devuelve una copia superficial de la lista:"""
print(cuadrados[:])
#[1, 4, 9, 16, 25]

#Las listas también soportan operaciones como concatenación:
print(cuadrados + [36, 49, 64, 81, 100])
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#A diferencia de las cadenas de texto, que son immutable, las listas son un tipo mutable, es posible cambiar un su contenido:
cubos = [1, 8, 27, 65, 125] # hay algo mal aquí
#4 ** 3 # el cubo de 4 es 64, no 65!
#64
cubos[3] = 64 # reemplazar el valor incorrecto
print(cubos)
#[1, 8, 27, 64, 125]
#También podés agregar nuevos ítems al final de la lista, usando el método append() (vamos a ver más sobre los métodos
#luego):
cubos.append(216) # agregar el cubo de 6
cubos.append(7 ** 3) # y el cubo de 7

print(cubos)
# [1, 8, 27, 64, 125, 216, 343]

# También es posible asignar a una rebanada, y esto incluso puede cambiar la longitud de la lista o vaciarla totalmente:
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(letras)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# REEMPLAZAR ALGUNOS VALORES
letras[2:5] = ['C', 'D', 'E']
print(letras)
# ['a', 'b', 'C', 'D', 'E', 'f', 'g']

# AHORA BORRARLAS
letras[2:5] = []
print(letras)
# ['a', 'b', 'f', 'g']


#BORRA LA LISTA  REEMPLAZANDO TODOS LOS ELEMENTOS POR UNA LISTA VACIA

letras[:] = []
print(letras) # []


#LA FUNCION PREDEFINIDA LEN PARA LISTAS
#La función predefinida len() también sirve para las listas:
letras = ['a', 'b', 'c', 'd']
len(letras) # 4


#ANIDAR LISTAS
#Es posible anidar listas (crear listas que contengan otras listas), por ejemplo:

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
# [['a', 'b', 'c'], [1, 2, 3]]

print(x[0]) 
#['a', 'b', 'c'] imprime el elemento indice 0 de x q es la lista a 

print(x[0][1]) # "b" Porque imprime del elento indice 0 de x q es la lista a. De esa lista imprimi el elemento indice 1 q es b

