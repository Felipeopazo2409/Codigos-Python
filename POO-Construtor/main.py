
from Coche import Coche #importamos la clase

carro = Coche("Rojo","Toyota","Yaris",200,1000,3)

carro.printData()

#Detectar tipado

if(type(carro)==Coche):
    print("Es un Objeto Correcto")
else:
    print("No es objeto!!")

#visibilidad
carro.soy_publico