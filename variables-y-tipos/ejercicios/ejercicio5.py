
numero1 = int (input("Ingrese numero 1: "))
numero2 = int(input("Ingrese numero 2: "))

if (numero1>numero2):
    print("Error!")
    numero1 = int (input("Ingrese numero 1: "))
    numero2 = int(input("Ingrese numero 2: "))
else:
    for i in range (numero1,numero2+1):
        if (i%2!=0):
            print(i)
        
