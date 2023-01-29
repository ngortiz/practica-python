#1.  se require un texto bienvenidos a pedidos ya
#2.  Se requiere mostrar un menu con sus respectivos precios
#3.  el usuario puede seleccionar uno o varios menu
#4.  el sistema debe mostrar el total a pagar
#5.  el usuario debe ingresar su dinero
#6.  el sistema debe imprimir el vuelto
#7.  el sistema debe decir al final gracias por la compra

print("!Bienvenidos a pedidos ya!")
print("Menu")
print("1. Pizza napolitana---- Gs.30.000")
print("2. Lomito simple------- Gs.20.000")
print("3. Hamburguesa simple---Gs.15.000")
print("4. Coca Cola de 1/2------Gs.5.000")
print("0. Presione 0 para finalizar su pedido")

pedido = []
total_pedido = 0
while True:
    producto = int(input("Seleccione el producto: "))
    if producto == 0:
        break
    cantidad = int(input("Cuanto: "))
    if producto > 4: 
        print("El producto seleccionado no exite")
        next
    pedido.append(producto)
    if producto == 1:
        total_pedido += (30000 * cantidad)
    elif producto == 2:
        total_pedido += (20000 * cantidad)
    elif producto == 3: 
        total_pedido += (15000 * cantidad)
    elif producto == 4:
        total_pedido += (5000 * cantidad)
print("Total a pagar Gs: " + str(total_pedido))
efectivo = int(input("Ingrese el efectivo: "))
vuelto = efectivo - total_pedido
print("Vuelto: " + str(vuelto))
print("Gracias por su compra!")
print("A continuacion se muestra detalle de su compra")
for producto in pedido: #[3,4]
    if producto == 1:
        print("Pizza Napolinata")
    elif producto == 2:
        print("Lomito simple")
    elif producto == 3:
        print("Hamburguesa simple")
    elif producto == 4:
        print("Coca cola de 1/2")
    

    


    
