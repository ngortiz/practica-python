# el usuario debe ingresar 5 numeros
#cada nro que ingresa dede almacenarce en una lista y al finalizar el programa debe imprimir 
#1.La longuitud de la lista len
#2.El primer elemento de la lista
#3.El ultimo elemento de la lista
# 4.La suma total de los elementos de la lista
# 5.Los numeros que son pares de la lista

numero = int(input("Ingrese el numero"))

# range(5)=> [0,1,2,3,4]
# 5=> str(5) => "5"
lista = []
#longuitud_de_lista_len = []
#primer_elemento_de_la_lista = []
#ultimo_elemento_de_la_lista = []
numeros_pares_de_la_lista = []
suma = 0
for item in range(numero):
    num = int(input("Ingresar un numero: "))
    lista.append(num)
    suma += num

    if num % 2 == 0:
        numeros_pares_de_la_lista.append(num)
    #print("Ingrese el numero" + str(item +1))
    #longuitud_de_lista_len = (input("len(lista"))
    #primer_elemento_de_la_lista = int(input("Ingrese el primer numero de la lista"))
    #ultimo_elemento_de_la_lista = int(input("Ingrese el ultimo numero de la lista"))
    #numeros_pares_de_la_lista =int(input("Ingrese los numero pares de la lista"))

print("la longitud de la lista es: " + str(len(lista)))
print("el primer elemento de la lista: " + str(lista[0])) # [4, 9, 0, 6] => 
print("el ultimo elemento de la lista es: " + str(lista[-1]))
print(" suma: " + str(suma))
for numero_par in numeros_pares_de_la_lista:
    print(numero_par)