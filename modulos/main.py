"""
    Modulos o librería: son funcionalidades ya hechas para reutilizar.

"""

#Importar modulo propio

#import mimodulo #importa todas las funciones
#from mimodulo import calculadora #importar una funcion de mi modulo

from mimodulo import * #Importa todas las funciones

print(calculadora(4,5))

#Modulo de fechas 

import datetime

print(datetime.date.today())
    
fecha_completa = datetime.datetime.now()
print(fecha_completa)

print(fecha_completa.year)
print(fecha_completa.month)

