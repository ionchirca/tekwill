'''1. Calculate when python course ends. Start date (28.10.2019) + 15 weeks + 8
days of vacation.'''

# from datetime import datetime, timedelta
# now = datetime.now()
# print(f"Python course ends on {datetime(2019, 10, 28) + timedelta(weeks=15) + timedelta(days=8)}")

'''2. Write a program which randomly picks an integer from 1 to 100. Your program
should prompt the user for guesses – if the user guesses incorrectly, it should
print whether the guess is too high or too low. If the user guesses correctly,
the program should print how many guesses the user took to guess the right
answer. You can assume that the user will enter valid input.''' 

# import random

# randNumber = random.randint(1, 100) 

# countAttempts = 0
# guess = input("Please guess the number between 1 and 100: > ")

# while True:
#     countAttempts += 1
#     if int(guess) == randNumber:
#         print(f"Congrats! {guess} is the right number."\
#               f" It tooks you {countAttempts} attempts to guess the number.")
#         break
#     elif int(guess) > randNumber:
#         guess = input("Try again, the number is less: > ")
#     elif int(guess) < randNumber:
#         guess = input("Try again, the number is bigger > ")

'''3. Download content of 999.md site, calculate how many urls are present on it.
(text with href="https content)'''

# from urllib.request import urlopen #deschiode o conexiune HTTP sa scoata date de pe site
# import re

# response = urlopen('https://999.md')
# for line in response:
#     line = line.decode('utf-8'), '\n'
#     ht = re.findall(r'href="http', str(line))
#     hts = re.findall(r'href="https', str(line))
#     print(f"Total HTTP links = {len(ht)}\nTotal HTTPS links = {len(hts)}")
#     print(f"Total number of HTTP and HTTPS links = {len(ht) + len(hts)}")

'''
4.1. Separate your project in files / modules, rewrite your program using import
functions
4.2. Create module for base class
4.3. Each animal class separate'''

from animals import zoo, reptiles, fishes, birds, mammals

zoo.Zoo.create_csv()

#Creem diferite tipuri de anumale
rep1 = reptiles.Reptiles('snake', 3, 'reptiles')
rep2 = reptiles.Reptiles('lizard', 4, 'reptiles')
rep3 = reptiles.Reptiles('alligator', 6, 'reptiles')

bird1 = birds.Birds('stork', 2, 'birds')
bird2 = birds.Birds('duck', 5, 'birds')
bird3 = birds.Birds('sparrow', 7, 'birds')

mamm1 = mammals.Mammals('lion', 7, 'mammals')
mamm2 = mammals.Mammals('tiger', 10, 'mammals')

fish1 = fishes.Fishes('eel', 4, 'fishes')


#Afisam numarul total de animale, prin doua metode
fish1.count()
mamm1.count()
rep1.count()

print(f"Num of total reptiles = {zoo.Zoo.reptiles}")
print(f"Num of total fishes = {zoo.Zoo.fishes}")

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


