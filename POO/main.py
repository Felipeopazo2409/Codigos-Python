
class Coche:
    #Atributos
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

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

  

    
# Fin definicion clase 

#Crear objetos /instanciar la clase
print("----Coche1------")
coche = Coche()
print(coche.marca)

#Crear mas objetos
print("----Coche2-----")
coche2 = Coche()
print(coche2.getColor())