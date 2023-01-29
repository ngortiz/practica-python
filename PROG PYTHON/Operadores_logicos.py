# Conjuncion

print("Conjuncion (and)")
num_uno = int(input("Escriba un numero mayor a 2 y menor a 5:"))
if num_uno > 2 and num_uno <5:
    print(" El numero ", num_uno, "cumple con la condicion.\n ")
else:
    print(" El numero ", num_uno, "cumple con la condicion.\n ")

#Dinyuncion
print("Disyuncion (or)")
palabra = input("Para cumplir con la condicion escribe 'si' o 'yes':")
if palabra == 'si' or palabra == 'yes':
    print("La condicion se ha cumplido.\n")
else:
    print("La condicion se ha cumplido.\n")

#Negacion
print("Negacion (not)")
num_uno = int(input("Introduce un numero igual a 5: "))
if not num_uno == 5:
    print("\n El numero es diferente a cinco y SI cumple las condicion.\n ")

else:
    print("\n El numero es diferente a cinco y NO cumple las condicion.\n ")
