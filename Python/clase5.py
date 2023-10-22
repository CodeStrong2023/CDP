"""#Ejercicio 5.1

print("Ingrese el rango de números para la suma")
a = int(input())
b = int(input())
sum = 0

for i in range(a,b+1):
    if i % 2 == 0:
        sum = sum+i

print(f"La suma total es", {sum})

#Ejercicio 5.2

a = int(input("Ingrese el número a factorizar"))
res = 1

for i in range(a,0,-1):
    res = res * i

print(f"El resultado factorial del número dado es", {res})


#Ejercicio 6

a = int(input("Ingrese el valor a multiplicar"))
lst = []
res = 1

for i in range(1,11):
    lst.append(i*a)

print ("La lista del número ingresado es: ", lst)
"""
#Ejercicio 7
import random

n = random.randrange(1,101)
x = None
while x != n:
    x = int(input("Ingrese un valor para intentar adivinar"))
    if x < n:
        print("El número es mayor")
    else:
        print("El númmero es menor")

print("Perfecto, el número es: ", n)
