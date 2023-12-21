### Fechas ###
import datetime # Importando el modulo fecha
from datetime import datetime   # Accediendo una funcion en especifica del modulo

ahora = datetime.now() # Inicializando el objeto de tipo datetime a través de la funcion now en una variable

def print_date(date):
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.month)
    print(date.year)
    print(date.timestamp())

print_date(ahora)

marca_de_tiempo = ahora.timestamp()  # inicializando la función timestamp
# timestamp permite mostrar una dato que representa un tiempo preciso o momento justo


year_2024 = datetime(2024, 1, 1)

print_date(year_2024)

from datetime import time # Accediendo a la función time
current_time = time(21, 8, 50)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)
print(f"{current_time.hour}:{current_time.minute}:{current_time.second}")

from datetime import date # Accediendo al objeto date
current_date = date(2023, 12, 20) # Función para la fecha de forma manual

print(current_date.day)
print(current_date.month)
print(current_date.year)
print(f"{current_date.day}/{current_date.month}/{current_date.year}")

current_date = date.today() # Objeto que permite obtener la fecha actual a traves de una variable
print(current_date)

## Realizando operaciones con las fechas
current_date = date(current_date.year, current_date.month - 1, current_date.day)
print(current_date.month)

diferencia = year_2024 - ahora
print(diferencia)
diferencia = year_2024.date() - current_date
print(diferencia)

# Objeto timedelta sirve para operar con diferentes fechas
from datetime import timedelta  # importando el objeto timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print(end_timedelta + start_timedelta)
print(end_timedelta - start_timedelta)
