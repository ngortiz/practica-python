print("Sistema para calcular el promedio de un alumno")
nombr
ee = input("Para comenzar, ¿Cual es tu nombre?: ")
matematica = int(input(nombre +"¿Cual es tu calificacion en matematicas?: "))
quimica = int(input(nombre + "¿Cual es tu calificacion en quimica?: "))
biologia = int(input(nombre + "¿Cual es tu calificacion en biologia?: "))
promedio = (matematica + quimica + biologia) / 3
promedio = int(promedio)
if promedio >= 6: 
    print('Felicidades'  + nombre + '"aprobaste" con un promedio de:', promedio)

print("Fin.")