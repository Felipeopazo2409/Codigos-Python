"""
    Diccionario:
    un tipo de dato que almacena un conjunto de datos.
    En formato clave > valor.
    Es parecido a un array asociativo o un objeto json.
"""
persona = {
    "nombre": "felipe",
    "apellidos":"opazo",
    "web": "felipeopazo.cl"
}
print(persona["apellidos"])

#Lista con diccionarios

contactos = [
    {
        'nombre': 'Antonio',
        'email': 'antonio@gmail.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@gmail.com'
    },
    {
        'nombre': 'Salvador',
        'email': 'salvador@gmail.com'
    }   
]

contactos[0]['nombre'] = "Antoñito"
print(contactos[0]['nombre'])

print("\n Listado de contactos\n")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}\n")