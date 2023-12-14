### Bucles ###
## While ##
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:   # Es opcional
    print("Mi condición es mayor o igual a 10")

print("La condición continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)
    
print("La ejecución continúa")

## Ciclo For ##
my_list = [35, 24, 62, 52, 30, 30, 17]
for element in my_list:
    print(element)

my_tuple = (36, 1.68, "Francisco", "Botardo", "Francisco")
for element in my_tuple:
    print(element)

my_set = {"Francisco", "Botardo", 36}
for element in my_set:
    print(element)

my_dict = {
    "Nombre":"Francisco",                           # Estructura de los diccionarios
    "Apellido":"Botardo",                           # clave valor
    "Edad":36, 
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1:1.68
    }
for element in my_dict:
    print(element)
    if element == "Edad":
        break   # Palabra reservada para detener la ejecución del bucle a partir de ese punto
    print("Se ejecuta")

else:
    print("El bucle For para mi diccionario ha finalizado.")