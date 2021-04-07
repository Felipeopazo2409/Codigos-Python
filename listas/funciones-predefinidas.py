
cantantes = ['2pac','Drake','Bad Bunny',"Reik"]

numeros = [1,2,5,8,3,4]

# Ordenar una lista 
print(numeros)
numeros.sort()
print(numeros)

#Agregar elementos

cantantes.append("Alex Ubago")
cantantes.insert(1,"David Bisbal")#Hay que elegir en que indice quieres agregar algo

#Eliminar Elementos
cantantes.pop(1) #Elimina por indice

cantantes.remove("Reik") # Elimina por elementos

#Dar la vuelta la lista

numeros.reverse()

#Buscar dentro de una lista 

print('Drake' in cantantes)#Devuelve un booleano

#Contar Elementos

print(len(cantantes))

# Cuantas veces aparece un elemento en una lista

print(numeros.count(8))

#Conseguir indice
print(cantantes.index("Drake"))

#Unir listas 
cantantes.extend(numeros)
