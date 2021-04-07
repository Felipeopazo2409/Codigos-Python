
class Coche:
    #Atributos
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    soy_publico = "Hola, SOY UN ATRIBUTO PUBLICO"
    __soy_privado = "Hola, soy un atributo privado"

    def __init__(self,color,marca,modelo,velocidad,caballaje,plazas):
        self.color = color
        self.modelo = modelo
        self.marca = marca
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
    
    def printData(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Velocidad: {self.velocidad}")
        print(f"Caballaje: {self.caballaje}")
        print(f"Plazas: {self.plazas}")

    def setColor(self,color):
        self.color = color
    
    def getColor(self):
        return self.color

    def setVelocidad(self,velocidad):
        self.velocidad = velocidad

    def getVelocidad(self):
        return self.velocidad


    def acelerar(self): #Con self puedo acceder a los atributos de mi clase
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1