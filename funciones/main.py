

def sumar (a,b):
    return a+b

print(sumar(1,2))

#Parametros Opcionales

def getEmpleado(nombre,dni = None):
    print("Empleado")
    print(f"Nombre: {nombre}")
    if(dni!=None):
        print(F"DnI: {dni}")

getEmpleado("Felipe Opazo",24)

#Funciones lambda Funciones lambda

dime_el_year = lambda year: f"El Año es {year}"
print(dime_el_year(2034))