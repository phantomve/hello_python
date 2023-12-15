### Clases ###
class MyEmptyPerson:   # Los nombres de las clases se escriben con cammel case
    pass               # Permite completar la clase persona sin generar ningun error

print(MyEmptyPerson)
print(MyEmptyPerson())


class Person:
    def __init__(self, name, surname, alias = "sin alias"):  # Constructor de clases, que permiten establecer ciertos valores relacionados a la clase persona
        self.full_name = f"{name} {surname} {alias}"
    
    def walk(self):
        print(f"{self.full_name} está caminando")

my_person = Person("Francisco", "Botardo")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Josreyn", "Botardo", "Francode")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "phantomve playing CS2"
print(my_other_person.full_name)