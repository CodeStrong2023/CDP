# ejercicio: dadas las horas trabajadas de 5 personas y la tarifa de pago, 
# calcular el salaio, y la sumatoria de todos los salarios 

salario_total = 0

for i in range(5):
    horas_trabajadas = float(input("digite las horas trabajadas de la persona {}: ".format(i + 1)))
    tarifa_pago = float(input("digite la tarifa de pago por hora de la persona {}: ".format(i + 1)))

    salario = horas_trabajadas * tarifa_pago
    salario_total += salario

    print("El salario de la persona {} es: {}".format(i + 1, salario))

print("La sumatoria de todos los salarios es: {}".format(salario_total))
