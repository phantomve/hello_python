### Manejo de Errores (Excepciones) ###
numberOne = 5
numberTwo = 1
numberTwo = "1"

try:
    print(numberOne + numberTwo)
    print("no se ha producido error")
except:
    # se ejecuta si se produce una excepción
    print("se ha producido un error")

#try except else finally
try:
    print(numberOne + numberTwo)
    print("no se ha producido error")
except:
    print("se ha producido un error")
else:       # opcional
    # se ejecuta si no se produce una excepción
    print("la ejecución continúa correctamente")
finally:    # opcional
    # se ejecuta siempre
    print("La ejecución continúa")

# Diferentes tipos de errores
try:
    print(numberOne + numberTwo)
    print("no se ha producido error")
except TypeError:   # except se ejecuta solo si es un typeError
    # se ejecuta si se produce una excepción
    print("se ha producido un TypeError")
except ValueError:  # except se ejecuta solo si es un error del tipo ValueError
    print("se ha producido un ValueError")

# Captura de la información de la excepción
try:
    print(numberOne + numberTwo)
    print("no se ha producido error")
except ValueError as error:     # almacena el tipo de error en una variable
    print(error)                # imprime la variable para indicar el error
except Exception as error:      # Muestra un tipo de error genérico en el programa
    print(error)