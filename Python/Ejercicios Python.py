#Clase 7
#Ejercicio 1: Estacion del año
mes = int(input("Ingrese un mes del ano(1/12): "))
verano =  3
otono = 6
invierno = 9
primavera = 12
if mes <= verano:
    print("La estacion es Verano")  
if mes > verano and mes <= otono:
    print("La estacion es Otono") 
if mes > otono and mes <= invierno:
    print("La estacion es Invierno")
if mes > invierno and mes <= primavera:
    print("La estacion es Primavera")  
else:
    print("El numero digitado no pertenece a un mes")


#Ejercicio 2: Etapas de la vida
edad = int(input("Ingrese su edad: "))
if edad > 0 and edad <= 9:
    print("La infancia es increible y bella")
elif edad > 9 and edad <= 19:
    print("Tienes muchos cambios, mucho que estudiar")
elif edad > 19 and edad <= 29:
    print("Amor y comienza el trabajo")
elif edad > 29 and edad <= 39:
    print("A disfrutar de la familia y los amigos")
else:
      print("etapa de vida no reconocida")


#Ejercicio 3: Sistema de Calificaciones
Nota = int(input("Ingrese su nota: "))
if Nota >= 9 or Nota <= 10:
    print("A")
elif Nota == 8:
    print("B")
elif Nota == 7:
    print("C")
elif Nota == 6:
    print("D")
elif 0 <= Nota < 6:
    print("F")



    #Clase 8
#Ejercicio 1
opcion = 0
while opcion != 1:
    a = int(input("Ingrese el ano: "))
    if a % 4 == 0 and a %100 != 0 or a % 100 == 0 and a % 400 == 0:
        print(f"El ano {a} es bisiesto")
    else:
        print(f"El ano {a} no es bisiesto")
    opcion = int(input("Si quiere salir del programa digite '1', si no digite '0': "))


#Ejercicio 2
num = int(input("Ingrese la cantidad de numeros a sumarse: "))
suma = 0
b = 0
while suma < num:
    suma += 1
    b = b + suma
else:
    print("Fin de la suma")
print(f"la suma es: {b}")


#Ejercicio 3
i = 0
np = 0
nn = 0
neg = 0
while i < 10:
    num = int(input("Digite un numero: "))
    i += 1
    if num > 0:
        np += 1
    elif num == 0:
        nn += 1
    elif num < 0:
        neg += 1
print(f"La cantidad de positivos es: {np}")
print(f"La cantidad de negativos es: {neg}")
print(f"La cantidad de neutros es: {nn}")


#Ejercicio 4
i = 0
suma = 0
cbaja = 11
prom = 0
while i < 10:
    nota=int(input("Digite una calificacion: "))
    i += 1
    suma = nota + suma
    if nota<cbaja:
        cbaja = nota
prom = suma/10
print(f"La calificacion promedio es: {prom}")
print(f"La calificacion mas baja es: {cbaja}")


#Ejercicio 5
num = int(input("Digite un numero: "))
if num >= 0:
    i = 1
    fact = 1
    while i <= num:
        fact = fact * i
        i += 1
    print(f"el factorial es: {fact}")
else:
    print("no se puede calcular el factorial")


#Ejercicio 6
n=int(input("Digite la cantidad de numeros a ingresar: "))
i = 1
sp = 0
cp = 0
si = 0
ci = 0
while i <= n:
    num=int(input("Digite un numero: "))
    if num % 2 == 0:
        sp = sp + num
        cp += 1
    else:
        si = si + num
        ci += 1
    i += 1
if cp != 0:
    print(f"La suma de los numeros pares es: {sp}")
    print(f"El conteo de los numeros pares es: {cp}")
else:
    print("No se han digitado numeros pares")
if ci != 0:
    print(f"La suma de los numeros impares es: {si}")
    print(f"El conteo de los numeros impares es: {ci}")
else:
    print("No se han digitado numeros impares")


#Ejercicio 7
i = 1
suma = 0
while i<= 5:
    print(f"Salario del empleado: {i}")
    horas=int(input("Digite las horas trabajadas: "))
    tarifa=int(input("Digite la tarifa por hora: "))
    salario = horas * tarifa
    print(f"El salario es de: {salario}")
    suma = suma + salario
    i += 1
else:
    print(f"La suma de todos los salarios es: {suma}") 