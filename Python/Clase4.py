# Ejercicio 1 Eliminar duplicados de la lista

lst = ["Hola", "Hello", "Chau", "Chau","Adios", "Bye", "Hola"]
unique_lst = []

for x in lst:
    if x not in unique_lst:
        unique_lst.append(x)

print(unique_lst)

# Ejercicio 2

lst_a = ["a", "b", "c", "d", "g", "h"]
lst_b = ["a", "c", "e", "f", "g", "h"] 
lst_unique = []
#1
all_lst = lst_a + lst_b

for i in all_lst:
    if i not in lst_unique:
        lst_unique.append(i)

print(lst_unique)

# Ejercicio 3 

lst = []
i = 0

while i == 0:
    x = int(input("Ingrese los valores de la lista"))

    if x != 0:
        lst.append(int(x))
    elif x == 0:
        i = 1

lst.sort()
print(lst)