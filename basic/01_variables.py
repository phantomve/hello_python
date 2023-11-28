## Variables

# variable tipo string
my_string_variable = "My String Variable"
print(my_string_variable)

# variable tipo entero
my_int_variable = 5
print(my_int_variable)

# Conviertiendo una variable entera en una cadena de texto
my_int_to_str_variable = str(my_int_variable) # Tipo str
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# variable tipo booleana
my_bool_variable = True
print(my_bool_variable)

# print con varios argumentos
# concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)

# concatenación de un texto con una variable
print("Este es el valor de:",my_bool_variable)

## Funciones del sistema

# funcion que retorna la cantidad de caracteres del argumento
print(len(my_string_variable))

# variables en una sola linea
name, surname, alias, age = "Francisco", "Botardo", "PhantoM", 36
print("Me llamo:", surname, name, "mi edad es:", age, "y mi alias es:", alias)


# funcion input() para entrada de datos
"""
name = input("¿Cual es tu nombre?\n")
age = input("¿Cuantos años tienes?\n")
print(name)
print(age)
"""

# cambiando el tipo de dato
name = 35
age = "Francisco"
print(name)
print(age)

# Forzando el tipo de dato a string
address: str = "mi direccion"