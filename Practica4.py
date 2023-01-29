cantidad_de_verduras = int(input("Cantidad de verduras: "))
verduras = []
for i in range(cantidad_de_verduras):
    verdura = input("Ingresar verdura: ")
    verduras.append(verdura)
print("Su canasta tiene", verduras)
