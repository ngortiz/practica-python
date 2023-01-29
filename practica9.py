# se desea tener un programa de stock para registrar mercaderias
# el sistema debe
# 1. solicitar al usuario cuantas mercaderias va a registrar
# 2. debe permitir ingresar el nombre y la cantidad por cada mercaderia
# 3. se desea saber cuantas mercaderias fueron registradas
cantidad_de_mercaderias = int(input("Ingrese cantidad de mercaderia a registrar"))
lista = []
total_de_mercaderias = 0
for item in range(cantidad_de_mercaderias):
    nombre_de_mercaderia = input("Ingresar el nombre de la mercaderia: ")
    cantidad = int(input("Ingresar cantidad de mercaderia: "))
    lista.append(nombre_de_mercaderia)
    total_de_mercaderias += cantidad
print("Suma total de merdarias" + str(total_de_mercaderias))



