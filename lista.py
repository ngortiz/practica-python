numero =[5,2,23, 55,1,2, 9,6]
frutas = ["Naranja", "Manzana", "Banana", "kiwi", "Mandarina", "uva", "naranja"]
#print(frutas)
#print(frutas[5])
#print(frutas[-6])
#print(frutas[1:5] )

#funciones de las listas
#list, len, append, extend, insert, remove, clear, pop, index,count, sort, reverse, copy
#lista = list(("hola", "adios", "chau"))
#print(lista)
print(len(frutas))
frutas.append("Piña")
print(frutas)
frutas[1]=("Piña")
print(frutas)
lista2 = numero + frutas
print(lista2)
numero.extend(frutas)
print(numero)
frutas.insert(2, "Piña")
print(frutas)
frutas.remove("kiwi")
print(frutas)
frutas.clear
print(frutas)
frutas.pop()
print(frutas)
frutas.index("Mandarina")
print(frutas)
frutas.count("Kiwi")
print(frutas)
numero.sort
print(numero)
numero.reverse
print(numero)
