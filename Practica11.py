print("Bievenido a calcuadora")
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero:"))

print("+. Suma")
print("-. Resta")
print("*. Multiplicacion")
print("/. Division")
operacion = input("Introduce la opcion deseada:")
if operacion == "+":
    suma = n1 + n2
    print("la suma es:" +str(suma))
elif operacion == "-":
    resta = n1 -n2 
    print("la resta es:" +str(resta))
elif operacion == "*":
    multiplicacion = n1 * n2 
    print("la multiplicacion es:" +str(multiplicacion))
elif operacion == "/":
    division = n1/n2 
    print("la division es:" +str(division))
