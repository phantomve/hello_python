### Tuplas ###
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (36, 1.68, "Francisco", "Botardo", "Francisco")
my_other_tuple = (65, 60, 35)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])      # Imprimiendo el indice 0 de la tupla
print(my_tuple[-1])     # Imprimiendo el indice -1 de la tupla
# print(my_tuple[4])    IndexError
# print(my_tuple[6])    IndexError

print(my_tuple.count("Francisco"))      # Del valor especificado cuenta cuantos se encuentran en la lista
print(my_tuple.index("Botardo"))        # Nos muestra en que indice se encuentra el valor especificado.

# my_tuple[0] = 1.70    # Error ya que las tuplas no se pueden reasignar.


my_sum_tuple = (my_tuple + my_other_tuple)  # Concatena tuplas
print(my_sum_tuple)

print(my_sum_tuple[3:7])    # Imprimiendo una porción de la tupla

# Convirtiendo una tupla al tipo lista
my_tuple = list(my_tuple)
print(type(my_tuple))       
my_tuple[4] = "FranCode"        # Al convertir la tupla a lista nos permite a reasignar valores
my_tuple.insert(1,"Azul")       # También nos permite a agregar nuevos valores por ser una lista
my_tuple = tuple(my_tuple)      # Revertimos el cambio convirtiendo la lista a tupla
print(my_tuple)
print(type(my_tuple))

# del my_tuple[2]               # No permite la eliminación de un indice especifico, ya que las tuplas no son modificables
del my_tuple                    # Eliminando la tupla creada
# print(my_tuple)               # Indica que no está definida ya que fue eliminada en el paso anterior

