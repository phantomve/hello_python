### Diccionarios ###
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Francisco", "Apellido":"Botardo", "Edad":36, 1:"Python"}

my_dict = {
    "Nombre":"Francisco",                           # Estructura de los diccionarios
    "Apellido":"Botardo",                           # clave valor
    "Edad":36, 
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1:1.68
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])        # Impresión del valor agregado en la clave Nombre

my_dict["Nombre"] = "Josreyn"   # Modificando el valor de la clave Nombre
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Direccion"] = "Maracay sector centro" # Agregando una nueva clave "campo" al diccionario
print(my_dict)

del my_dict["Direccion"]        # Eliminar un valor especifico de nuestro diccionario
print(my_dict)

print("Nombre" in my_dict)      # Verificar si un tipo de valor se encuentra en el diccionario
print("Francisco" in my_dict)

# Métodos de los diccionarios
print(my_dict.items())          # Nos muestra un listado de cada uno de los items
print(my_dict.keys())           # Retorna un listado de las llaves "keys" en formato lista
print(my_dict.values())

my_new_dict = my_other_dict.fromkeys(("Nombre", 1)) # Crea un diccionario nuevo sin valores
print(my_new_dict)

# Crando un diccionario desde una lista con fromkeys
my_list = ["Nombre", "Apellido", 1]
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)    # Pasando a nuevo diccionario las claves de un diccionario preaviamente creado
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "FranCode")    # Pasando valores al diccionaro, genera los mismos valores para cada una de las llaves, no sería utilizable
print(my_new_dict)

print(list(my_new_dict))    # Imprime una lista con las keys del diccionario
print(tuple(my_new_dict))   # Imprime una tupla con las keys del diccionario
print(set(my_new_dict))     # Imprime un set con las keys del diccionario
print(my_new_dict.values()) # Imprime los valores del diccionario

my_values = my_new_dict.values()    # listado de valores
print(type(my_values))
print(list(my_new_dict.values()))   # Imprime una lista de los valores del diccionario