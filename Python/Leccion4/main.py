# CLASE 1 video 1

# Colecciones en Python

# Las listas es lo que se conoce en otros lenguajes como arreglos o vectores

# lista = ariel, liliana, natalia, osvaldo

nombres = ["naty", "osvaldo", "lili", "ariel"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])  # (para ver el ulitmo de la lista)

# video 2

print(nombres)
print(nombres[0:2])  # solo muestra el indice 0, 1 pero no el indice 2
# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[1:])

# Modificamos un valor

nombres[2] = "liliana"
nombres[0] = "natalia"
print(nombres)

# Iterar una lista

for nombre in nombres:  # nombre es singular, la lista es plural
    print(nombre)
else:
    print("se acabaron los elementos de la lista")

# video 3

# Preguntamos cuantos elementos tiene

print(len(nombres))  # le pasamos como parametro la lista

# agregamos un elemento

nombres.append("marcelo")
print(nombres)

# Insertar un elemento en un indice especifico

nombres.insert(1, "alberto")
print(nombres)
nombres.insert(3, "debora")
print(nombres)

# Eliminamos un elemento

nombres.remove("alberto")
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un indice especifico

del nombres[2]  # del significa delete (eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos

nombres.clear()
print(nombres)

# Eliminar la lista

del nombres
# print(nombres)  # nos salta un error por que ya borro la lista!

# video 4 en EjercicioRango.py

# video 6

# Definimos una tupla
cocina = "cuchara", "cuchillo", "tenedor"
print(cocina)
print(len(cocina))

# Acceder a un elemento,para esto utilizamos corchetes no parentesis

print(cocina[0])

# Mostrar de manera inversa

print(cocina[-1])

# Acceder a un rango

print(cocina[0:1])

# EJEMPLO

verduras = ("papa",)  # una tupla necesita aunque sea de un elemento la coma (,)
# de lo contrario solo seria un tipo string cadena

# video 7

for cocinar in cocina:  # print esta usando \n para saltos de linea
    print(cocinar, end=" ")  # Usamos end= para eliminar saltos de linea

"""cocina[0] = "plato"  # da error
print(cocina)

cocinalista = list(cocina)
cocinalista[0] = "plato"
cocina = tuple(cocinalista)
print("\n", cocina)

del cocina  # esto es para eliminar
print(cocina)
"""
# CLASE 2
# #video 1 y 2
# Tipo set (orden alertorio)(y no se repiten elementos)
planetas = {"marte", "jupiter", "venus"}  # ejemplo
print(len(planetas))  # usamos la funcion len= length significa largo

# revisar si un elemento eciste dentro de set
print("marte" in planetas)  # respetar mayusculas,minusculas y acentos

# agregar un elemento
planetas.add("tierra")  # add es una funcion
print(planetas)

# Eliminar elementos, puede generar un error si el elemento no existe

planetas.remove("jupiter")  # esta funcion ante un mal ingreso del elemanto da error
print(planetas)

planetas.discard("tierra")  # esta funcion no nos presenta ningun error

# limpiar set

planetas.clear()
print(planetas)

# Eliminar set o conjunto

# del planetas # da error por que borra el set

# video 3

# 'maradona' :10 Un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(key,value)
diccionario = {
    "IDE": "Integrated development environment",
    "POO": "Programacion orientada a objetos",
    "SABD": "Sisitema de Administracion de base de datos",
}
print(len(diccionario))  # len se usa para verificar la cantidad de elementos
print(diccionario)

# acceder a un diccionario con la llave (key)

print(diccionario["IDE"])

# otra forma de recuperar un elemento
print(diccionario.get("POO"))
print(diccionario.get("SABD"))

# modificamos elementos
diccionario["IDE"] = "Entorno de desarrollo integrado"
print(diccionario)

# video 4
# como recorrer los elementos
for termino in diccionario:
    print(termino)

for termino in diccionario:  # recorremos mostrando solo las llaves
    print(termino)
for termino, valor in diccionario.items():
    print(termino, valor)

# otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino)  # muestra solo las llaves

for valor in diccionario.values():  # usamos una funcion para acceder al valor
    print(valor)

# comprobar la ecistencia de algun elemento
print("IDE" in diccionario)  # devuelve un booleano

# agregar un elemento
diccionario["PK"] = "Primary key"
print(diccionario)

# eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

# vaciar un diccionario
diccionario.clear()
print(diccionario)

# eliminar diccionario
del diccionario  # el diccionario se borra
# print(diccionario)  # da error por que se borro en la linea anterior

# video 5 explica que a las listas se les puede agregar cualquier tipo de dato.

# video 6

# concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2
print(lista3)

lista3.extend([7, 8, 9, 1])  # funcion para aggregar varios elementos a una lista
print(lista3)

print(lista3.index(5))  # funcion para ubicar en que indice esta el valor ingresado
# print(lista3.index(0)) #esto daria un error por no ser el elemento parte de la lista

# como saber cuantos valores repetidos hay dentro de una lista

print(lista3.count(1))  # cuenta cuantos avlores iguales hay dentro de la lista

# para poner una lista al reves

lista3.reverse()
print(lista3)

# video 7

# para que una lista se multiplique repitiendo sus elementos

lista3 = lista3 * 2
print(lista3)

# Metodos de ordenamiento

lista3.sort()  # ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True)  # ordena los elementos descendentemente
print(lista3)

# video 8

# repaso de tuplas

tupla = (
    3,
    "hola",
    6.78,
    [1, 2, 78],
    4,
    "hola",
)  # puede tener diferentes tipos de datos dentro
print(tupla)
print(4 in tupla)  # accuin booleana, su respuesta es de tipo booleana
# lo que podemos usar dentro de tuplas son: index, count, len
# en tuplas se puede convertir de tupla a lista y de lista a tupla


# CLASE 3
# video 1

# repaso de set o conjunto
# para definir un conjunto
conjunto2 = set()
conjunto1 = {
    "bye",
}
conjunto2.add(7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add("hola")
print(conjunto1)
print(3 not in conjunto1)  # preguntamos  si el numero 3 NO esta en el conjunto1

# como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2)  # nos devuelve como respuesta un booleano

# operaciones en conjuntos

conjunto3 = conjunto1 | conjunto2  # la linea une los dos conjuntos
print(conjunto3)

conjunto3 = (
    conjunto1 & conjunto2
)  # que elemento tienen en comun (signo raro que no se cual es xD)
print(conjunto3)

conjunto3 = (
    conjunto1 - conjunto2
)  # asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)

conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = (
    conjunto1 ^ conjunto2
)  # elemento que no comparten o que son diferentes esntre ambos
print(conjunto3)

# video 3

conjunto3 = conjunto1 | conjunto2
print(
    conjunto2.issubset(conjunto3)
)  # aqui preguntamos si un conjunto es subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(
    conjunto3.issuperset(conjunto1)
)  # preguntamos si los elementos del conjunto1 estan dentro del 3
print(
    conjunto3.issubset(conjunto2)
)  # si es verdadero quiere decir que ele conjunto3 es un superconjunto
print(conjunto2.issubset(conjunto3))

# como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2))  # no hay cosas en comun

# convertir un conjunto totalmente inmutable

conjunto1 = frozenset  # esto hace que el conjunto sea totalmente inmutable
# no se puede agregar,modificar ni eliminar del conjunto.

# video 4

# Repaso diccionarios

diccionarioNuevo = {
    "azul": "blue",
    "rojo": "red",
    "verde": "green",
    "amarillo": "yellow",
}
print(diccionarioNuevo)

# como eliminar
del diccionarioNuevo["azul"]
print(diccionarioNuevo)

# los diccionarios pueden almavenar diferentes tipos de datos
diccionario2 = {
    "ariel": {"edad": 40, "altura": 1.83},
    "osvaldo": [45, 1.85],
    "natalia": [35, 167],
}
print(diccionario2)

# video 5

seleccionArgentina = {
    10: {
        "nombre": "Lionel Messi",
        "edad": 35,
        "altura": 1.70,
        "precio": "300 millones",
        "Posicion": "Extremo derecho",
    },
    11: {
        "nombre": "Angel di Maria",
        "edad": 34,
        "altura": 1.80,
        "precio": "100 millones",
        "Posicion": "Extremo izquierdo",
    },
    24: {
        "nombre": "Paulo Dybala",
        "edad": 28,
        "altura": 1.77,
        "precio": "98 millones",
        "Posicion": "Media punta",
    },
    19: {
        "nombre": "Nicolas Otamendi",
        "edad": 34,
        "altura": 1.83,
        "precio": "70 millones",
        "Posicion": "Central",
    },
    1: {
        "nombre": "Rodrigo de Paul",
        "edad": 29,
        "altura": 1.77,
        "precio": "80 millones",
        "Posicion": "Mediocampista",
    },
    29: {
        "nombre": "Gonzalo Ariel Montiel",
        "edad": 26,
        "altura": 1.75,
        "precio": "12 millones",
        "Posicion": "Lateral derecho",
    },
    8: {
        "nombre": "Enzo Fernández",
        "edad": 22,
        "altura": 1.72,
        "precio": "200 millones",
        "Posicion": "Mediocampista",
    },
    18: {
        "nombre": "Lucas Beltrán",
        "edad": 22,
        "altura": 1.78,
        "precio": "120 millones",
        "Posicion": "Delantero",
    },
    9: {
        "nombre": "Julian Alvarez",
        "edad": 23,
        "altura": 1.77,
        "precio": "180 millones",
        "Posicion": "extremo derecho",
    },
}

for llave in seleccionArgentina.items():
    print(llave, valor)

# como tarea agregar por lo menos 4 jugadores mas al diccionario: seleccionArgentina
print("tenemos cargados en el diccionario la cantidad de : ", end=" ")
print(len(seleccionArgentina))

# video 5

# pilas usando lista
pila = [1, 2, 3]

# agregar elementos a la pila por el final

pila.append(4)
pila.append(5)
print(pila)

# sacando elementos desde el final

elementoBorrado = pila.pop()  # quita el ultimo elemento y lo guarda en la variable
print(f"Sacamos el elemento {elementoBorrado}")
print(f"La pila ahora quedo asi: {pila}")

# video 6

# colas en listas

# Estructura de datos de tipo fgifi (first input / first output)

cola = ["ariel", "osvaldo", "liliana", "pilar"]

# agregamos elementos al final de la cola

cola.append("natalia")
cola.append("jose")
print(cola)

# sacamos elementos de la cola

seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)
seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)
seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)
seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)
seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)
