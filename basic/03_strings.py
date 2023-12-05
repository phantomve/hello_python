### Strings ###
my_string = "Mi String"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un string \n escapado"
print(my_scape_string)

## Formateo ##
name, surname, age = "Francisco", "Botardo", 36
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombes es {name} {surname} y mi edad es {age}")

## Desempaquetado de caracteres ##
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

## División ##
language_slice = language[1:3]
print(language_slice)

language_slice = language[0:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverso #
reversed_language = language[::-1]
print(reversed_language)

## Funciones del Sistema ##
print(language.capitalize())

print(language.upper())

print(language.count("t"))

print(language.isnumeric())
print("2".isnumeric())

print(language.lower())

print(language.upper().islower())

print(language.startswith("py"))
