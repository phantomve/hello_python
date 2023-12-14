### Funciones ###

# Función simple
def my_function ():
    print("Esto es una función")

my_function ()
my_function ()
my_function ()

# Función que suma tanto tipo int como stings
def sum_two_values (first_value, second_value):
    print(first_value + second_value)

sum_two_values (5, 7)
sum_two_values ("457", "368")

# Función que retorna
def sum_two_values_with_return (first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(10, 5)
print(my_result)

# Función tipo string con parámetros invertidos
def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname = "Botardo", name = "Francisco")

# Función con parámetros por defecto
def print_name_with_default (name, surname, alias = "Sin Alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default ("Francisco", "Botardo")

# Función que recibe varios parámetros
def print_texts(*texts):
    for text in texts:
        print(text)

print_texts("Hola", "Python", "Francode")
