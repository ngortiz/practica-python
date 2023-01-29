print("*************************************************************************")
print("Programa para determinar ¿ cual es el numero mas grande de tres numero?: ")
print("*********************************************************************** \n.")
num_uno = int(input("Intoduce el primer numero:"))
num_dos = int(input("Intoduce el segundo numero:"))
num_tres = int(input("Intoduce el tercero numero:"))

if num_uno > num_dos and num_uno > num_tres:
    print("El numero", num_uno, "es el numero mas grande de los tres.")
else: 
    if num_dos > num_tres:
        print("El numero ", num_dos, "es el numero mas grande de los tres.")
    else:
      print("El numero ", num_tres, "es el numero mas grande de los tres.")
