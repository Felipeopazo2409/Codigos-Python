
def holamundo(nombre):
    return f"Hola que tal estas, {nombre}"


def calculadora(numero1,numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2 
    multiplicar = numero1 * numero2
    division = numero1/numero2

    cadena = ""
    cadena+="Suma: "+str(suma)
    cadena+="\n"
    cadena+="Resta: "+str(resta)
    cadena+="\n"
    cadena+="Multiplicación: "+str(multiplicar)
    cadena+="\n"
    cadena += "Division: "+str(division)

    return cadena
