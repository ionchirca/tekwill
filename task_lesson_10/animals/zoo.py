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
