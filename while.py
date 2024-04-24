"""""
Primeros pasos hacia la programación
Por supuesto, podemos usar Python para tareas más complicadas que sumar dos y dos. Por ejemplo, podemos escribir una
subsecuencia inicial de la serie de Fibonacci así:
"""
# SERIES DE FIBONACCI
#  la suma de dos elementos define el siguiente
 
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b

"""
1
1
2
3
5
8


Este ejemplo introduce varias características nuevas.

• La primer línea contiene una asignación múltiple: las variables a y b toman en forma simultanea los nuevos valores 0
y 1. En la última linea esto se vuelve a usar, demostrando que las expresiones a la derecha son evaluadas antes de
que suceda cualquier asignación. Las expresiones a la derecha son evaluadas de izquierda a derecha.
• El bucle while se ejecuta mientras la condición (aquí: b < 10) sea verdadera. En Python, como en C, cualquier
entero distinto de cero es verdadero; cero es falso. La condición también puede ser una cadena de texto o una lista,
de hecho cualquier secuencia; cualquier cosa con longitud distinta de cero es verdadero, las secuencias vacías son
falsas. La prueba usada en el ejemplo es una comparación simple. Los operadores estándar de comparación se
escriben igual que en C: < (menor qué), > (mayor qué), == (igual a), <= (menor o igual qué), >= (mayor o igual
qué) y != (distinto a).
• El cuerpo del bucle está sangrado: la sangría es la forma que usa Python para agrupar declaraciones. En el intérprete
interactivo debés teclear un tab o espacio(s) para cada línea sangrada. En la práctica vas a preparar entradas más
complicadas para Python con un editor de texto; todos los editores de texto decentes tienen la facilidad de agregar la
sangría automáticamente. Al ingresar una declaración compuesta en forma interactiva, debés finalizar con una línea
en blanco para indicar que está completa (ya que el analizador no puede adivinar cuando tecleaste la última línea).
Notá que cada línea de un bloque básico debe estar sangrada de la misma forma.
• La función print() escribe el valor de el o los argumentos que se le pasan. Difiere de simplemente escribir la
expresión que se quiere mostrar (como hicimos antes en los ejemplos de la calculadora) en la forma en que maneja
múltiples argumentos, cantidades en punto flotante, y cadenas. Las cadenas de texto son impresas sin comillas, y un
espacio en blanco es insertado entre los elementos, así podés formatear cosas de una forma agradable:
"""

i = 256*256
print('El valor de i es', i)

"""El valor de i es 65536
El parámetro nombrado end puede usarse para evitar el salto de linea al final de la salida, o terminar la salida con una
cadena diferente:"""
a, b = 0, 1

while b < 1000:
    print(b, end=',')
    a, b = b, a+b

1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,

"""Debido a que ** tiene mayor precedencia que -, -3**2 será interpretado como -(3**2) y eso da como
resultado -9. Para evitar esto y obtener 9, podés usar (-3)**2.
3 A diferencia de otros lenguajes, caracteres especiales como \n tiene el mismo significado con simple ('...') y
doble ("...") comillas. La única diferencia entre las dos es que dentro de las comillas simples no tenés la
necesitada de escapar " (pero tenés que escapar \') y viceversa."""