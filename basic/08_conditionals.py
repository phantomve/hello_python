### Condicionales ###
my_condition = False

if my_condition:    # es lo mismo que  if my_condition == True:
    print("Se ejecuta la condición del if")

my_condition = 5 * 5

# Condicionales simples
if my_condition == 10:  
    print("Se ejecuta la condición del segundo if")

if my_condition > 10:  
    print("Se ejecuta la condición del segundo if")

# Condicional compuesto
if my_condition > 10:  
    print("Es mayor que diez")
else:
    print("Es menor o igual a diez")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que diez y menor que 20")
else:
    print("Es menor  o igual a 10 o mayor o igual a 20")

# ELIF
if my_condition > 10 and my_condition < 20:
    print("Es mayor que diez y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor  o igual a 10 o mayor o igual a 20")

my_string = "Mi cadena de texto"

if my_string:
    print("Mi cadena de texto no está vacía")

if my_string == "Mi cadena de textoooo":
    print("Estas cadena de texto coinciden")

print("La ejecución continúa")
