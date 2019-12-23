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
3. Try to separate type of animals in base / child Class, use inheritance
  in order to group common animals attributes.
4. Store each new created animal in a list / dictionary, write a function
  that will find all animals of a certain class
"""

import csv

class Zoo:
    '''Creem o clasa parinte(Zoo) care va ajuta la crearea unui obiect
    (sau tip de animal) iar la creare va fi obligator(by default) de specificat
    numele, virsta si specia'''

    mammals = 0; fishes = 0; birds = 0; reptiles = 0

    def __init__(self, name, age, species, count = 0):
        self.name = name
        self.age = age
        self.species = species
        with open('zoo.csv', 'a') as append_animal:
            append = csv.writer(append_animal)
            append.writerow([self.name, self.age, self.species,\
                            None, None, None, None])

    '''Acesta este o functie ajutatoare pentru a putea vedea info despre
    obiectul creat, ex. fara __repr__ (print(rept1)
    = <__main__.Reptiles object at 0x7f217b8>) ex. cu ___repr__ (print(rept1)
    = (Additional info: age:3, class:reptiles))'''
    def __repr__(self):
        return f"(Additional info: age:{self.age}, class:{self.species})"

    ''' Acesta metoda este de tip class method, adica functia data nu poate
    accesa atributele definite mai sus in clasa (atributele obiectului),
    ea poate lucra doar cu atribute definite in ea'''
    @classmethod
    def date_of_birth(cls, birthday):
        cls.birthday = birthday
        return cls.birthday
    
    def count(self):
        '''Acesta metoda intoarce numarul total de animale definite pentru o 
        specie, rezultatul poate fi obtinut prin doua metode'''
        if self.species == 'reptiles':
            print(f"Number of total defined {self.species} = {Zoo.reptiles}")
        elif self.species == 'birds':
            print(f"Number of total defined {self.species} = {Zoo.birds}")
        elif self.species == 'mammals':
            print(f"Number of total defined {self.species} = {Zoo.mammals}")
        elif self.species == 'fishes':
            print(f"Number of total defined {self.species} = {Zoo.fishes}")

    @staticmethod
    def create_csv():
        '''Acesta metoda este utilizata pentru a crea/recrea fisierul csv,
        acest fisier este o baza de date cu info despre animale'''
        with open('zoo.csv', 'w') as zoofile:
            write = csv.writer(zoofile)
            write.writerow(['Name', 'Age', 'Species', 'Birthday', 'Food',\
                           'Tail Length', 'Skin Color'])

    def food(self, food):
        '''Aceasta metoda este utilizata pentru a defini tipul de mincare 
        specific pentru fiecare animal, apoi il stocheaza in fisierul csv'''
        self.food = food
        print(f"{self.name.title()} can eat {self.food}")
        new_data = []
        with open('zoo.csv', 'r') as read:
            read = csv.reader(read)
            for line in read:
                if line[0] == self.name:
                    line[4] = self.food
                    new_data.append(line)
                else:
                    new_data.append(line)
            with open('zoo.csv', 'r+') as write:
                write = csv.writer(write)
                write.writerows(new_data)

'''Mai jos avem o clasa copil, care mosteneste toate atributele si
metodele(functiile) din clasa parinte + putem defini alte metode, atribute
specifice acestei clase'''
class Mammals(Zoo):

    food = ['meat', 'plants']

    def __init__(self, name, age, species):
        super().__init__(name, age, species)
        Zoo.mammals += 1

    def food(self, food):
        super().food(food)

    def date_of_birth(self, birthday):
        super().date_of_birth(birthday)
        return f"{self.name.title()} is {self.age} years old"\
               f" with birthday on {self.birthday}"

class Birds(Zoo):

    food = ['insects', 'worms', 'grubs' 'seeds', 'grasses', 'plant material']

    def __init__(self, name, age, species):
        super().__init__(name, age, species)
        Zoo.birds += 1

    def food(self, food):
        super().food(food)

    def date_of_birth(self, birthday):
        super().date_of_birth(birthday)
        return f"{self.name.title()} is {self.age} years old"\
               f"with birthday on {self.birthday}"

class Fishes(Zoo):

    food = ['smaller fish', 'worms', 'crustaceans',\
           'small organisms', 'plant matter']

    def __init__(self, name, age, species):
        super().__init__(name, age, species)
        Zoo.fishes += 1

    def food(self, food):
        super().food(food)

    def date_of_birth(self, birthday):
        super().date_of_birth(birthday)
        return f"{self.name.title()} is {self.age} years old"\
               f"with birthday on {self.birthday}"

class Reptiles(Zoo):

    food = ['meat', 'fruits', 'insects', 'eggs']

    def __init__(self, name, age, species):
        super().__init__(name, age, species)
        Zoo.reptiles += 1

    def food(self, food):
        super().food(food)

    @staticmethod
    def write_to_csv(item1, item2, item3):
        '''Metoda face update la fisierul csv, ea este chemata pentru 
        a actualiza culoarea si lungimea cozii reptilelor definite'''
        new_data = []
        with open('zoo.csv', 'r') as read:
            read = csv.reader(read)
            for line in read:
                if line[0] == item1:
                    line[item2] = item3
                    new_data.append(line)
                else:
                    new_data.append(line)
            with open('zoo.csv', 'r+') as write:
                write = csv.writer(write)
                write.writerows(new_data)

    def color(self, color):
        self.color = color
        print(f"{self.name.title()} has {self.color} color")
        Reptiles.write_to_csv(self.name, 6, self.color)

    def tail_length(self, length):
        self.length = length
        print(f"{self.name.title()} tail length is {self.length} cm")
        Reptiles.write_to_csv(self.name, 5, self.length)

    def date_of_birth(self, birthday):
        super().date_of_birth(birthday)
        return f"{self.name.title()} is {self.age} years old"\
               f"with birthday on {self.birthday}"



''' Metoda data este statica si utilizata pentru a crea/recrea fisierul csv,
la recreare(chemare) ea sterge tot continutul si creaza doar prima linie'''
Zoo.create_csv()

#Creem diferite tipuri de anumale
rep1 = Reptiles('snake', 3, 'reptiles')
rep2 = Reptiles('lizard', 4, 'reptiles')
rep3 = Reptiles('alligator', 6, 'reptiles')

bird1 = Birds('stork', 2, 'birds')
bird2 = Birds('duck', 5, 'birds')
bird3 = Birds('sparrow', 7, 'birds')

mamm1 = Mammals('lion', 7, 'mammals')
mamm2 = Mammals('tiger', 10, 'mammals')

fish1 = Fishes('eel', 4, 'fishes')


#Afisam numarul total de animale, prin doua metode
fish1.count()
mamm1.count()
rep1.count()

print(f"Num of total reptiles = {Zoo.reptiles}")
print(f"Num of total fishes = {Zoo.fishes}")

# Adaugam in fisierul CSV tipul de mincare specific pentru fiecare animal
# Afisam rezultatul la ecran
rep2.food(['insects', 'flies', 'worms'])
bird1.food(['snake', 'reptiles'])


# Asignam o culoare pentru un tip de reptila si o stocam in fisierul CSV
# Afisam rezultatul la ecran
rep3.color('green')
rep1.color('gray')


# Asignam lungimea cozii pentru un tip de reptila si o stocam in fisierul CSV
# Afisam rezultatul la ecran
rep1.tail_length(3)


