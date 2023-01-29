print("*******************************")
print("Sistema nacional de catastro \n")
print("*******************************")
usuario = input("Ingrese su nombre:")

print("1. Paraguayo")
print("2. Argentino")
print("3. Brasilero")
print("4. Chileno")
nacionalidad = int(input("Introduce la opcion deseada:"))

if nacionalidad == 1:
    print( usuario + " es Paraguayo")
elif nacionalidad == 2:
    print(usuario + " es Argentino")
elif nacionalidad == 3:
    print(usuario + " es Brasilero")
elif nacionalidad == 4:
    print(usuario + " es Chileno")
else:
     print("La opcion elegida no existe, vuelve a intentarlo.")
