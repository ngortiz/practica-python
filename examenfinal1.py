def sumadevalores(lista, valor_limite):
    suma_de_valores = 0
    posicion = 1
    for num in lista:
        if num >= valor_limite:
            break
        if posicion%2 == 0: 
            suma_de_valores = suma_de_valores + num
        posicion = posicion + 1 
    print(suma_de_valores)


#lista = [1,2,4,6,92,56]
#valor_limite = 90
#sumadevalores(lista,valor_limite)

#suma = 0
lista = [26, 71, 42, 25, 48, 52, 61, 17, 67, 41, 25, 66, 44, 62, 45, 2, 12, 51, 70, 73, 11, 34, 36, 35, 37, 5, 64, 48, 39, 16, 15, 83, 21, 71, 55, 58, 12, 73, 59, 10, 3, 83, 17, 2, 10, 64, 42, 47, 72, 54, 14, 70, 8, 57, 85, 65, 79, 33, 73, 65, 14, 10, 81, 83, 35, 50, 15, 54, 20, 80, 30, 52, 56, 28, 4, 79, 55, 59, 8, 77, 45, 3, 76, 42, 78, 77, 30, 71, 16, 86, 54, 10, 41, 4, 88, 8, 78, 28, 47, 83, 73, 90, 44, 34, 15, 7, 62, 58, 38, 35, 72, 50, 63, 56, 23, 3, 36, 58, 51, 74, 46, 78, 69, 79, 23, 89, 24, 78, 82, 18, 55, 32, 12, 19, 8, 86, 53, 70, 62, 49, 86, 87, 75, 72, 86, 97, 96, 99, 100, 92]
limite = 92
sumadevalores(lista, limite)