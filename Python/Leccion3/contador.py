# EJERCICIO 3: leer 10 numeros  e imprimir cuantos son positivos 
#,cuantos negativos y cuantos neutros. 

positivos = 0
negativos = 0
neutros = 0

for i in range(10):
    numero = float(input("Ingresa un número: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        neutros += 1

print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
print("Cantidad de números neutros:", neutros)
