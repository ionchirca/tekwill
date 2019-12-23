from animals import zoo

class Birds(zoo.Zoo):

    food = ['insects', 'worms', 'grubs' 'seeds', 'grasses', 'plant material']

    def __init__(self, name, age, species):
        super().__init__(name, age, species)
        zoo.Zoo.birds += 1

    def food(self, food):
        super().food(food)

    def date_of_birth(self, birthday):
        super().date_of_birth(birthday)
        return f"{self.name.title()} is {self.age} years old"\
               f"with birthday on {self.birthday}"
