# Cadenas de caracteres

print('huevos y pan') # comillas simples
'huevos y pan'

#'doesn\'t' # usa \' para escapar comillas simples...
#"doesn't"

print("doesn't") # ...o de lo contrario usa comillas doblas
print("doesn't")

print('"Si," le dijo.') # '"Si," le dijo.'

print("\"Si,\" le dijo.") # '"Si," le dijo.'

print('"Isn\'t," she said.')#'"Isn\'t," she said.'

"""En el intéprete interactivo, la salida de cadenas está encerrada en comillas y los caracteres especiales son escapados con
barras invertidas. Aunque esto a veces luzca diferente de la entrada (las comillas que encierran pueden cambiar), las dos
cadenas son equivalentes. La cadena se encierra en comillas dobles si la cadena contiene una comilla simple y ninguna
doble, de lo contrario es encerrada en comillas simples. La función print() produce una salida más legible, omitiendo las
comillas que la encierran e imprimiendo caracteres especiales y escapados:"""
print('"Isn\'t," she said.') #'"Isn\'t," she said.'

print('"Isn\'t," she said.') #"Isn't," she said.
 
s = 'Primerea línea.\nSegunda línea.' # \n significa nueva línea

print(s) # con print(), \n produce una nueva línea

#Primera línea.
#Segunda línea.
#Si no querés que los caracteres antepuestos por \ sean interpretados como caracteres especiales, podés usar cadenas
#crudas agregando una r antes de la primera comilla:

print('C:\algun\nombre') # aquí \n significa nueva línea!
#C:\algun
#ombre
print(r'C:\algun\nombre') # nota la r antes de la comilla  C:\algun\nombre
#Las cadenas de texto literales pueden contener múltiples líneas. Una forma es usar triple comillas: """...""" o
#'''...'''. Los fin de línea son incluídos automáticamente, pero es posible prevenir esto agregando una \ al final de la
#línea. Por ejemplo:

print("""\
Uso: algo [OPTIONS]
 -h Muestra el mensaje de uso
 -H nombrehost Nombre del host al cual conectarse
""")

#produce la siguiente salida: (nota que la línea inicial no está incluída)
#Uso: algo [OPTIONS]
# -h Muestra el mensaje de uso
# -H nombrehost Nombre del host al cual conectarse
#Las cadenas de texto pueden ser concatenadas (pegadas juntas) con el operador + y repetidas con *:
 # 3 veces 'un', seguido de 'ium'
print(3 * 'un' + 'ium') #'unununium'

#Dos o más cadenas literales (aquellas encerradas entre comillas) una al lado de la otra son automáticamente concatenadas:
print('Py' 'thon') #'Python'


#Si querés concatenar variables o una variable con un literal, usá +:
prefix = "py"
print(prefix + 'thon') #'Python'

#Esta característica es particularmente útil cuando querés separar cadenadas largas:
texto = ('Poné muchas cadenas dentro de paréntesis '
 'para que ellas sean unidas juntas.')
print(texto) #Poné muchas cadenas dentro de paréntesis para que ellas sean unidas juntas.

#Las cadenas de texto se pueden indexar (subíndices), el primer carácter de la cadena tiene el índice 0. No hay un tipo de
#dato para los caracteres; un carácter es simplemente una cadena de longitud uno:

palabra = 'Python'
print(palabra[0]) # caracter en la posición 0 "p"

print(palabra[5]) # caracter en la posición 5 'n'

#Los índices quizás sean números negativos, para empezar a contar desde la dereche:
print(palabra[-1]) # último caracter  'n'

print(palabra[-2]) # ante último caracter  'o'

print(palabra[-6]) # caracter en la posición -6  'P'

"""Nota que -0 es lo mismo que 0, los índice negativos comienzan desde -1.
Además de los índices, las rebanadas también están soportadas. Mientras que los índices son usados para obtener
caracteres individuales, las rebanadas te permiten obtener sub-cadenas:"""

print(palabra[0:2]) # caracteres desde la posición 0 (incluída) hasta la 2 (excluída) 'Py'

print(palabra[2:5]) # caracteres desde la posición 2 (incluída) hasta la 5 (excluída) 'tho'

"""Nota como el primero es siempre incluído, y que el último es siempre excluído. Esto asegura que s[:i] + s[i:] siempre
sea igual a s:"""
print(palabra[:2] + palabra[2:]) #'Python'

print(palabra[:4] + palabra[4:]) #'Python'

"""Los índices de las rebanadas tienen valores por defecto útiles; el valor por defecto para el primer índice es cero, el valor por
defecto para el segundo índice es la longitud de la cadena a rebanar."""

print(palabra[:2]) # caracteres desde el principio hasta la posición 2 (excluída) 'Py'


print(palabra[4:]) # caracterrs desde la posición 4 (incluída) hasta el final 'on'

print(palabra[-2:]) # caracteres desde la ante-última (incluída) hasta el final 'on'

"""Una forma de recordar cómo funcionan las rebanadas es pensar en los índices como puntos entre caracteres, con el punto
a la izquierda del primer carácter numerado en 0. Luego, el punto a la derecha del último carácter de una cadena de n
caracteres tienen índice n, por ejemplo:
+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+
0 1 2 3 4 5 6
-6 -5 -4 -3 -2 -1
La primer fila de números da la posición de los índices 0...6 en la cadena; la segunda fila da los correspondientes índices
negativos. La rebanada de i a j consiste en todos los caracteres entre los puntos etiquetados i y j, respectivamente.
Para índices no negativos, la longitud de la rebanada es la diferencia de los índices, si ambos entran en los límites. Por
ejemplo, la longitud de palabra[1:3] es 2.
Intentar usar un índice que es muy grande resultará en un error:"""

"""palabra[42] # la palabra solo tiene 6 caracteres
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
IndexError: string index out of range"""
#Sin embargo, índices fuera de rango en rebanadas son manejados satisfactoriamente:
print(palabra[4:42]) #'on'

print(palabra[42:]) #''

"""Las cadenas de Python no pueden ser modificadas -- son immutable. Por eso, asignar a una posición indexada de la
cadena resulta en un error:"""
"""
palabra[0] = 'J'
 ...
TypeError: 'str' object does not support item assignment
palabra[2:] = 'py'
 ...
TypeError: 'str' object does not support item assignment
Si necesitás una cadena diferente, deberías crear una nueva:
'J' + palabra[1:]
'Jython'
>>> palabra[:2] + 'py'
'Pypy'  """

#La función incorporada len() devuelve la longitud de una cadena de texto:"""

s = 'supercalifrastilisticoespialidoso'
print(len(s))


