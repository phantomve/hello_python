### Retos ###
"""
Reto #1: EL FAMOSO "FIZZ BUZZ”
 Escribe un programa que muestre por consola (con un print) los
 números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz". 
"""
def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)

fizzbuzz()

"""
RETO #2: ¿ES UN ANAGRAMA?
Escriba una funcion que reciba dos palabras (string) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un anagrama consiste en formar una palabra reordenando todas
las letras de otra palabra inicial.
- No hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    else:
        print(sorted(word_one.lower())) # reordena la palabra en letras tipo lista
        print(sorted(word_one.lower()))
        return sorted(word_one.lower()) == sorted(word_two.lower())
    
print(is_anagram("Amor", "Roma"))

"""
Reto #3: LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
"""

""" def fibonacci():
    j = 0
    l = 1
    print(j)
    print(l)
    for i in range(51):
       k = j + l
       print(k)
       j = l
       l = k """

def fibonacci():

    prev = 0
    next = 1

    for index in range(0, 51):
        print(prev)
        fib = prev + next      
        prev = next
        next = fib

fibonacci()


"""
Reto #4: ¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def is_prime():
    for number in range (1, 101):
        if number >= 2:

            is_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break
            
            if not is_divisible:
                print(number)
   
is_prime()

"""
RETO #7: INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def string_reverse(text):
    text_len = len(text)
    reversed_text = ""
    for index in range(0, text_len):
        reversed_text += text[text_len -index -1] 
    return reversed_text

print(string_reverse("hola mundo"))

