from animals import zoo

'''Mai jos avem o clasa copil, care mosteneste toate atributele si
metodele(functiile) din clasa parinte + putem defini alte metode, atribute
specifice acestei clase'''
class Mammals(zoo.Zoo):

    food = ['meat', 'plants']

    def __init__(self, name, age, species):
        super().__init__(name, age, species)
        zoo.Zoo.mammals += 1

    def food(self, food):
        super().food(food)

    def date_of_birth(self, birthday):
        super().date_of_birth(birthday)
        return f"{self.name.title()} is {self.age} years old"\
               f" with birthday on {self.birthday}"
