def sucesion(numero):
  suma = 0
  for n in range(1, numero + 1):
    suma = suma + n
  
  return suma

lista = [613, 562, 764, 518, 445, 692, 763]
suma = 0
for i in lista:
  suma = suma + sucesion(i)

from math import log
numero_de_log = 362797056
base_log = 6
log_base_j = log(numero_de_log, base_log)
resultado = suma * log_base_j
print(resultado)



