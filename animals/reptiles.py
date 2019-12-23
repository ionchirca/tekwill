import csv
from animals import zoo

class Reptiles(zoo.Zoo):

    food = ['meat', 'fruits', 'insects', 'eggs']

    def __init__(self, name, age, species):
        super().__init__(name, age, species)
        zoo.Zoo.reptiles += 1

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