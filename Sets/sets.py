"""
    Set es un tipo de datos, para tener  una coleccion de valores,
    pero no tiene ni indice ni orden 
"""
personas = {
    "Felipe",
    "Victor",
    "Francisco"
}

personas.add("Paco")
personas.remove("Francisco")
print(type(personas))
print(personas)