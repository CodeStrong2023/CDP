# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuacion elimine los elementos repetidos.

# Creamos una lista
lista = [1, 2, 3, "Ariel", 7, 7, 3, "Alberto", 5, "Ariel"]
# conjunto = set(lista)  # convertimos la lista a un conjunto de tipo set
# lista = list(conjunto)  # convertimos el conjunto en una lista
lista = list(set(lista))  # aca en una linea lo de arriba
print(lista)
