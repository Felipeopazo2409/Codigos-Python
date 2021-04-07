

pelicula = "Batman"
##Definir Una lista
peliculas = ["Batman","Spiderman","Superman"]
#En una tupla la informacion no se puede modificar, en cambio en una lista zi
cantantes = list(('2pac',"Drake","Alex Ubago"))#Le pasamos un tupla

years = list(range(2020,2050))

variada = ["Felipe",30,4.4,True,"Texto"]

#print(pelicula)
#print(years)
#print(variada)

#Indices
print(peliculas[0])
print(peliculas[-2])#se puede trabajar con indices negativos
print(cantantes[1:3])#Te saca informacion del indice 1 al 3

#Añadir elemto a lista 

cantantes.append ("Ozuna")#Agrega un elemento a la lista

print(cantantes)

#Recorrer Lista
nueva_pelicula = ""
while(nueva_pelicula!= "parar"):
    nueva_pelicula = input("Ingrese una pelicula")
    if(nueva_pelicula!="parar"):
        peliculas.append(nueva_pelicula)
    



print("****Listado de Peliculas****")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1} . {pelicula}")


#listas multidimensionales

print("\n******Listado de contactos *******")

contactos = [
    [
        'Antonio',
        'antonio@gmail.com'
    ],
    [
        'Luis',
        'Luis@gmail.com'
    ],
    [
        'Felipe',
        "Felipe@gmail.com"

    ]
]
print(contactos[1][1])



