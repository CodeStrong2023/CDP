"""#Ejercicio 10

lst = []
a = input("Ingrese una cadena de texto")

for i in a:
    if not i in lst:
        lst.append(i)
    
print(lst)
"""
#Ejercicio 11

contact = {}
n = None

while n != 4:
    print("Menú de acciones, seleccione cual quiere usar:")
    print("1 - Agregar contacto")
    print("2 - Borrar contacto")
    print("3 - Ver contactos")
    print("4 - Apagar")
    
    n = int(input())
    
    if n == 1:
        print("Indique nombre y luego el número del usuario")
        a = input()
        b = int(input())
        contact[a] = b
    elif n == 2:
        a = input("Indique que contacto quiere borrar")
        contact.pop(a)
    elif n == 3:
        print(contact)
    