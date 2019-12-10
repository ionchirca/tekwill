"""
Declare a class that will describe a Car with following attributes, year, fuel
type, color. Add to your class methods for calculating car’s age, retrieving fuel
type and setting new color."""



# class Car:
#
#     def __init__(self, year, fuel, color):
#         self.year = year
#         self.fuel = fuel
#         self.color = color
#
#
#     def carInfo(self):
#         return 2019 - self.year, self.fuel
#
#
# car1 = Car(1989, 'diesel', 'red')
#
# print(car1.carInfo())



"""
Declare a class that will describe a Student, it will have an attribute named
student grade and class method that will receive a list of grades and will
return a new Student objects with average of grades
"""


# class Student:
#
#     def __init__(self, listGrades, grade):
#         self.listGrades = listGrades
#         self.grade = grade
#
#     def averageGrades(self):
#         for i in self.listGrades:
#             self.grade += i / len(self.listGrades)
#         return self.grade
#
# ion = Student([5, 6, 7, 8], 0)
#
# print(ion.averageGrades())



# class Student:
#     grade = 0
#
#     def __init__(self, listGrades):
#         self.listGrades = listGrades
#
#     def averageGrades(self):
#         for i in self.listGrades:
#             self.grade += i / len(self.listGrades)
#         return self.grade
#
# ion = Student([5, 6, 7, 8])
#
# print(ion.averageGrades())

"""
Project
1. Create a database for a Zoo, each animal will have following characteristics:
- Name, age, class (mammals, birds, fishes, reptiles),
2. Add following methods:
- Initialization / Creation ( use __init__ method )
- Initialization / creation by date of birth (use class method)
- For each class of animal add methods that will display his favourite food.
- For reptiles add methods for changing color and length of it’s tail attribute.
3. Try to separate type of animals in base / child Class, use inheritance in order to group
common animals attributes.
4. Store each new created animal in a list / dictionary, write a function that will find all
animals of a certain class
"""

"""Este nevoie sa creezi o classa parinte unde o sa ai elementele comune (age, name, species class), 1 metoda de initializare (init) si o metoda de intializare cu ajutorul la data nasterii
 apoi sa creezi 3 clase care sa mosteneasca de la clasa parinte (Birds, Mamals, Fishes, Reptiles)
Fiecare clasa copil trebuie sa defineasca 1 metoda care o sa afiseze mincarea la specie
In clasa parinte este nevoie de creat o metoda care o sa intorca numarl de animale pentru fiecare specie"""


class Animals:

    def __init__(self, age, name, specie):
        self.age = age
        self.name = name
        self.specie = specie

    @classmethod
    def dateofBirth(cls):
        cld.birthday = birthday

    def numofAnimals():
        count = 0
        for self.specie:
            count += self.specie
        return count

class Birds(Animals):

    def __init__(self, food):
        self.food = food

    def Count(self):
        super().numofAnimals()


class Mammals(Animals):

    def __init__(self, food):
        self.food = food

class Fishes(Animals):

    def __init__(self, food):
        self.food = food

class Reptiles(Animals):

    def __init__(self, food, color, taillength):
        self.food = food
        self.color = color
        self.taillength = taillength
