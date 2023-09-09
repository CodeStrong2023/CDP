# EJERCICIO: Diseñar un programa que ingresado un año, nos devuelva
# por consola si es un ario bisiesto o no, repetir la accion
# hasta que el usuario 10 decida.

def es_bisiesto(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

contador = 0

while contador < 10:
    # Solicitar al usuario ingresar un año
    año = int(input("Ingresa un año: "))

    # Verificar si el año es bisiesto o no
    if es_bisiesto(año):
        print(año, "es un año bisiesto")
    else:
        print(año, "no es un año bisiesto")

    contador += 1
