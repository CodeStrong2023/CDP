# Ejercicio 3 : Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos
# Nombre: Aragon
# Clase: Herrero
# Raza: Dunadan del norte

# Nombrde: Gandalf
# Clase: Mago
# Raza: Istar

# Nombrde: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

personajes = []  # creamos una lista vacia
# creamos diccionarios
P = {"Nombre": "Aragon", "Clase": "Guerrero", "Raza": "Dunadan del norte"}
personajes.append(P)  # agregamos a la lista un personaje
P = {"Nombre": "Gandalf", "Clase": "Mago", "Raza": "Istar"}
personajes.append(P)
P = {"Nombre": "Legolas", "Clase": "Arquero", "Raza": "Elfo Sindar"}
personajes.append(P)
# agregamos los 3 personajes de la tarea
P = {"Nombre": "Boromir", "Clase": "Humano", "Raza": "Hombre de Gondor"}
personajes.append(P)
P = {"Nombre": "Galadriel", "Clase": "Elfo", "Raza": "Elfo Noldorin"}
personajes.append(P)
P = {"Nombre": "Frodo", "Clase": "Hobbit", "Raza": "Hobbit"}
personajes.append(P)
print(
    personajes
)  # Tarea: Agregar por lo menos otros 3 personajes que sea a tu eleccion.
