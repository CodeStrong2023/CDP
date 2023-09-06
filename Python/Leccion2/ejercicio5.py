# EJERCICIO 5: calcular el factorial de un numero mayor o igual a 0. (grupal)

def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

# Solicitar al usuario ingresar un número
numero = int(input("Ingresa un número: "))

# Verificar si el número es válido (mayor o igual a 0)
if numero >= 0:
    # Calcular el factorial
    factorial_resultado = factorial(numero)
    print("El factorial de", numero, "es:", factorial_resultado)
else:
    print("El número debe ser mayor o igual a 0 para calcular su factorial.")
