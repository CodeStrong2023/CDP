#Ejercicio 4

a = int(input("Ingrese el valor sin impuestos a calcular: "))

def calculo(a):
    total = a + a * (21/100)
    return total

resultado = calculo(a)

print("El pago total con impuestos sería de: ", resultado)

#Ejercicio 5

print("Elija que fórmula aplicar")
print("1- C a F")
print("2- F a C")

opcion = int(input())

valor = int(input("Ingrese el valor a convertir"))

def transformacion(opcion, val):
    total = None
    if opcion == 1:
        total = (val*1.8) + 32
        print("El valor en F es: ", total)
    elif opcion == 2:
        total = (val-32) / 1.8
        print("El valor en F es: ", total)
