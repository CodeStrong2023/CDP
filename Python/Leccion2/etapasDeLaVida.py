# EJERCICIO 4 CLASE 7 (etapas de la vida segun la edad)
edad = int(input('digite su edad: '))
mensaje = None
if 0 <= edad < 10: #sintaxis simplificada
    mensaje = 'la infancia es increible y bella'
elif 10 <= edad < 20:
    mensaje = 'tienes muchos cambios, mucho que estudiar'
elif 20 <= edad < 30:
    mensaje = 'amor y comienza el trabajo'
elif 30 <= edad < 40:
    mensaje = 'amor y comienza el trabajo'
elif 40 <= edad < 50:
    mensaje = 'amor y comienza el trabajo'
elif 50 <= edad < 60:
    mensaje = 'amor y comienza el trabajo'    
elif 60 <= edad < 70:
    mensaje = 'amor y comienza el trabajo'
elif 70 <= edad < 80:
    mensaje = 'amor y comienza el trabajo'
elif 80 <= edad < 90:
    mensaje = 'amor y comienza el trabajo'            
print(f"tu edad es: {edad}, {mensaje} ")

