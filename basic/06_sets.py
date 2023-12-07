### Sets ###
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))       # Inicialmente indica que es un diccionario

my_other_set = {"Francisco", "Botardo", 36}
print(type(my_other_set))       # Cuando se ingresan valores el diccionario vacio lo reconoce como un set

print(len(my_other_set))        # Cuenta la cantidad de valores incluidos en el set

my_other_set.add("FranCode")    # Ingresa un nuevo valor al set

print(my_other_set)             # Un set no es una estructura ordenada, por ello no permite imprimir un indice en específico.

my_other_set.add("FranCode")    # Un set no admite valores repetidos.
print(my_other_set)

# Busquedas (Formas de comprobar si un valor existe dentro de un set)
print("Francisco" in my_other_set)
print("Frank" in my_other_set)

my_other_set.remove("Botardo")  # remove permite eliminar valores específicos.
print(my_other_set)

my_other_set.clear()            # Clear elimina todo los elementos del set
print(len(my_other_set))

del my_other_set                # del elimina el ojbeto set por completo
# print(my_other_set)           # Indica error ya que fue eliminado el set en el paso anterior.

my_set = {"Francisco", "Botardo", 36}
my_list = list(my_set)
print(my_list)

my_other_set = {"python", "javascript", "Go"}

# Los sets no admiten repetidos.
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"typescript", "C#"}))

print(my_new_set.difference(my_set))    # Elimina los elementos que se encuentren en el set indicado.

