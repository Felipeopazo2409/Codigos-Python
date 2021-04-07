
class Persona:
    """
    nombre
    apellidos
    altura 
    edad
    """
    def getNombre(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apellidos
    
    def getEdad(self):
        return self.edad
    
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def setApellidos(self,apellidos):
        self.apellidos = apellidos

    def setEdad(self,edad):
        self.edad = edad
        
    def hablar(self):
        return "Estoy hablando"
    def dormir(self):
        print("Estoy durmiendo")


class Informatico(Persona):
    def __init__(self):
        super().__init__() #Aqui invoco los atributos
        self.lenguajes = "Html, Css, Javascript, PHP"
        self.experiencia = 5

    def getLennguajes(self):
        return self.lenguajes
    def aprender(self,lenguajes):
        self.lenguajes = lenguajes
    
    def programar(self):
        return "Estoy programando"

    