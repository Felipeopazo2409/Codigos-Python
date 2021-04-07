

texto = " "

if(len(texto.strip())<=0):
    print("La variable está vacia")
    texto = input("Ingrese texto a la variable: ")
else:
    print(f"Contenido de la variable {texto}")