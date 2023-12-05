### Operadores ###

print(3 + 4)    # Suma
print(3 - 4)    # Resta
print(3 * 4)    # Multiplicación
print(3 / 4)    # División
print(10 % 2)   # Módulo
print(10 // 3)  # División entera
print(2 ** 3)   # Exponente
print(2 ** 3 + 3 - 7 / 1 // 4)

# Concatenación de string
print("Hola" + " Python" + " ¿Que tal?")

# Concatenación de string y dato int convertido en string
print("Hola " + str(5))
print("Hola "*5)

# Fira code font
## Operadores Aritméticos ##
print(3 > 4)    # mayor que
print(3 < 4)    # menor que
print(3 >= 4)   # mayor o igual que
print(4 <= 4)   # menor o igual que
print(3 == 4)   # igual que
print(3 != 4)   # distinto que

# Regla de los operadores aritméticos para datos tipo string
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")             # ordenación alfabética
print(len("hola") >= len("zola"))   # contando caracteres
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

## Operadores Lógicos ##
print (3 > 4 and "Hola" > "Python")
print (3 > 4 or "Hola" > "Python")
print (3 < 4 and "Hola" < "Python")
print (3 < 4 or ("Hola" > "Python" and 4 == 4))
print (not(3 > 4))