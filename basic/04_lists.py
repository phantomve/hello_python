### Listas ###
my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [36, 1.68, "Francisco", "Botardo"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list[-4])
print(my_list.count(30))      # Retorna la cantidad de ocurrencias de un valor
# print(my_other_list[4])     # IndexError: list index out of range
# print(my_other_list[-5])    # IndexError: list index out of range

# Desempaquetando la lista
age, height, name, surname = my_other_list
print(name)

# Sumando Listas (Concatenando)
print(my_list + my_other_list)
# print(my_list + my_other_list) # Error

# Metodos para añadir elementos a la lista
my_other_list.append("FranCode")    # append inserta un elemento al final de la lista
my_other_list.insert(1, "Rojo")     # insert agrega un elemento en el indice que le indiquemos
my_other_list[1] = "Azul"           # Modifica el valor del indice indicado de la lista
print(my_other_list)

# Método para eliminar valores de la lista
my_other_list.remove("Azul")         # remove elimina el valor que le indiquemos de la lista
print(my_other_list)

my_list.remove(30)
print(my_list)
print(my_list.pop())                # pop elimina el ultimo valor agregado en la lista
print(my_list)
my_pop_element = my_list.pop(-2)    # pop está eliminando un valor en el indice especificado, y ademas lo está almacenando en una variable
print(my_pop_element)
print(my_list)
del my_list[2]                      # del elimina por indice un elemento de la lista, indicada sin almacenar el elemento.
print(my_list)

# Otros Métodos de listas
my_new_list = my_list.copy()        # Realiza una copia de la lista indicada
my_list.clear()                     # Elimina todo los valores de la lista
print(my_list)
print(my_new_list)
my_new_list.reverse()               # Reordena los valores de la lista en sentido contrario
print(my_new_list)         
my_new_list.sort()                  # Ordena de mayor a menor la lista
print(my_new_list)
print(my_new_list[1:2])             # Muestra una porcion de la lista de acuerdo a los parámetros especificados
print(my_new_list[1:3])              