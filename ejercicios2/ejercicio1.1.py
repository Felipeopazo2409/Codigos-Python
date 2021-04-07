
list_numbers = [3,5,1,7,8,0,10,9]

print("*****Printing numbers******")
for number in list_numbers:
    print(number)

#order of list 

list_numbers.sort()
print("List ordenaned")
print(list_numbers)

#Size of list

print(f"size = {len(list_numbers)}")

element = input("Input Element: ")

if(element in list_numbers):
    print("Se ha encontrado en la lista")
else:
    print("El elemento no existe")


