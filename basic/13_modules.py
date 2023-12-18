### Módulos ###
import my_module    # Importa las operaciones de otros ficheros para no repetir el codigo


my_module.sum(5, 4, 3)
my_module.printValue("Hello Python!")

from my_module import printValue, sum   # Importa solo la funcion en concreto, no todo el fichero.

sum(5, 3, 1)
printValue("Hi Python!")

import math # Importando libreria propia de python

print(math.pi)
print(math.pow(2,8))

from math import pi as PI_VALUE # Importando una función en específica a través de un alias

print(PI_VALUE)