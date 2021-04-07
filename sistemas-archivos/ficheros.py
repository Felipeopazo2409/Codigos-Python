from io import open
import pathlib
import shutil
import os
#abrir archivo

ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt" #Busca la ruta
print(ruta)
archivo = open(ruta,"a+")
#Escribir
archivo.write("********soy un texto metido desde python*********\n")

#Cerrar Archivo

archivo.close()


#Abrimos archivo para leerlo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt" #Busca la ruta

archivo_lectura = open(ruta,"r")

#Leer Contenido

#contenido = archivo_lectura.read()

#Leer contenido y guardar en lista

lista = archivo_lectura.readlines() # Crea una lista por cada linea que lee

print(lista)

archivo_lectura.close()

for frase in lista:
    print(f"- {frase}")
"""
#Copiar 
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt" #Busca la ruta
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_alternativa = "./paquetes/fichero_copiado.txt"
shutil.copyfile(ruta_original,ruta_alternativa)
"""