'''
miVariable = 3

print(miVariable)

miVariable = "hola a todo los alumnos de la tecnicatura"

print(miVariable)

miVariable = 3.5

print(miVariable)

x = 10

y = 2

z = x + y
print(id(x))

////////////////////////////////////////

#tipos int,float string, bool

x = 10
print(x)

print(type(x))

x = 14.5
print(x)

print(type(x))

x = "hola profe"
print(x)

print(type(x))

x = True
print (x)

print(type(x))

x = False
print(x)

print(type(x))

////////////////////////////////////////
# manejo de cadenas (String)


miGrupoFavorito = "los wachiturros"

caracteristica = "caquita"

print("Mi grupo favorito es: ", miGrupoFavorito ,caracteristica)


numero1 = "7"

numero2 = "8"

print(int(numero1) + int(numero2))

////////////////////////////////////////

#tipos boleanos (bool)


miBooleano = 1 < 2

print(miBooleano)


if miBooleano: 

    print("el resultado es verdadero")

else:

    print("el resultado es falso")
    
   

#procesar la entrada del usuario 
    

#funcion input

  #regresa un dato tipo String
#resultado = input("digite un numero: ") #regresa un dato string
#print(resultado)

# conversion de la entrada de datos
numero1 = int(input("escribe el primer numero: "))
numero2 = int(input("escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ",resultado)

''' # //////////////////////////////////
'''
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
#print ("resulatdo de la suma es: ",suma)
print(f"El resultado de la suma es: {suma}")

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multiplicacion = operandoA * operandoB 
print(f"el resultado de la multiplicaicon es: {multiplicacion}")

division = operandoA / operandoB
print(f"el resultado de la division es: {division}")

division = operandoA // operandoB
print(f"el resultado de la division (int) es: {division}")


modulo = operandoA % operandoB
print(f"el resultado de la division o residuo (moulo) es: {modulo}")

exponente = operandoA ** operandoB
print(f"el resultado del exponente es: {exponente}")

/////////////////////////////////////////////////
'''
'''
alto = int(input('proporciona el alto del rectangulo: '))
ancho = int(input('proporciona el anho del rectangulo: '))
area = alto * ancho
perimetro = (alto + ancho) * 2
print(f"area: {area}")
print(f"perimetro: {perimetro}")



miVariable3 = 10
print(miVariable3)

#operadores de resignacion

miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable3 * 2
miVariable3 *= 2
print(miVariable3)

# miVariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)

//////////////////////////////////////////


d = 4
b = 2
resultado = d == b # comprobamos si son iguales
print(resultado)

#operador diferente

resultado = d != b
print(resultado)

#operador mayor que

resultado = d > b
print(resultado)

resultado = d < b
print(resultado)

# Operador menor o igual que
resultado = d <= b
print(resultado)

#operador mayor o igual que
resultado = d >= b
print(resultado)

////////////////////////////////////////////////////
EJERCICIO 1

a = int(input("digite un numero: "))
print(f"El residuo de la div ision es: {a % 2}")
if a % 2 == 0:
    print(f"el valor de a es: {a} es un numero PAR. ")
else:
    print(f"el valor de a es: {a} es un numero IMPAR. ")
    
    
////////////////////////////////////////////////////

#EJERCICIO 2
    
edadAdulto = 18
edadPersona = int(input("digite su edad: "))
if edadPersona >= edadAdulto:
    print(f"su edad es: {edadPersona} años, usted es mayor de edad.")
else:
    print(f"su edad es: {edadPersona} años, usted es menor de edad.")

/////////////////////////////////////////////////////


a = True
b = True
resultado = a and b
print(resultado)
    

#operador or

resultado = a or b
print(resultado)

#operador not

resultado = not a
print(resultado)   

/////////////////////////////////////////////////////


# EJERCICIO: VALOR DENTRO DE UN RANGO

valor =int(input("digite un numero dentro del rango 0 a 5: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f"El valor {valor} ESTA dentro del rango") 
else:
    print(f"El valor {valor} NO esta dentro del rango")
    
/////////////////////////////////////////////////////

# EJERCICIO CON EL OPERADOR OR, OPERADOR NOT

vacaciones = True
diaDescanso = True
if not (vacaciones or diaDescanso):
    print("tiene trabajo que hacer")
else:
    print("puede asistir al juego")
    
   

# EJERCICIO: RANGO ENTRE 20 Y 30 AÑOS.

edad = int(input("digite su edad: "))
veinte = edad >= 20 and edad < 30
print(veinte)
treinta = edad >= 30 and edad < 40 
print(treinta)

if veinte or treinta:
    print("ESTAS dentro del rango de los (20\'0) a (30\'0) años")
else:
    print("NO dentro del rango de los (20'0) a (30'0) años")


 #EJERCICIO : EL MAYOR DE DOS NUMEROS. 
num1 = int(input("digite el valor para el numero1: "))
num2 = int(input("digite el valor para el numero2: "))

if num1 > num2:
    print("el numero 1 es mayor ")
else:
    print("el numero 2 es mayor ")



# EJERCICIO: TIENDA DE LIBROS

print("digite los siguientes datos del libro")
nombre = input("digite el nombre del libro: ")
id = int(input("digite el id del libro: "))
precio = float(input("digite el precio del libro: "))
envioGratuito = input("indicar si el envio es gratuito (true/False): ")
if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = "el valor es incorrecto, debe escribir True/False"
   
print(f'''
      
    #Nombre: {nombre}
    #Id: {id}
    #Precio: {precio}
    #Envio Gratuito?: {envioGratuito}   
    # ''') 
    
     

    
 

    









    

















