''' Scrieti o functie care sa gaseasca maximum a 3 numere '''

# def maximum(*args):
#     print(max(args))
#
# maximum(4, 68, 23, 7678, 4567, 878, 453)

'''Scrieti o functie care sa calculeze produsul elementelor unei liste. '''

# def prod(*args) -> list():
#     result = 1
#     for item in list(args):
#         result = result * item
#     print(result)
#
# prod(4, 5, 10)

'''Scrieti o functie care sa calculeze numarul de litere majuscule si minuscule
dintr-un text'''

# def numLetters(text):
#     listUpper = []
#     listLower = []
#     listOther = []
#     for item in text:
#         if item.isupper():
#             listUpper.append(item)
#         elif item.islower():
#             listLower.append(item)
#         else:
#             listOther.append(item)
#     print("Total number of uppercases is %s" % len(listUpper))
#     print("Total number of lowercases is %s" % len(listLower))
#     print("Total number of other characters including spaces is %s" %len(listOther))
#
# numLetters("Some RanDom TEXT, and Something ElSe!")

''' Scrieti o functie care sa intoarca elementele distincte dintr-o lista
Ex ([1,2,3,3,3,3,4,5] - > [1, 2, 3, 4, 5]) '''

# text = input("Type some text that will contain non unique values >>> ")
# def distinctElements(text):
#     myList = text.split()
#     uniqList = []
#     for item in myList:
#         if item not in uniqList:
#             uniqList.append(item)
#     print("The list with unique elements will be %s" % uniqList)
#
# distinctElements(text)


'''Scrieti o functie care calculeaza daca un numar este prim.'''


# number = input("Please insert a random number bigger than 0 >>> ")
# def primeNum(number):
#     myList = []
#     myNum = int(number)
#     for item in range(2, myNum):
#         if myNum % item != 0:
#             myList.append(1)
#         elif myNum % item == 0:
#             myList.append(0)
#     if 0 in myList:
#         print(f" {myNum} IS NOT a prime number")
#     else:
#         print(f" {myNum} IS a prime number")
#
# primeNum(number)



'''Scrieti o functie care afiseaza o secventa de numere Fibonacci
Numerele Fibonacci sunt definite prin următoarea relație de recurență:
Astfel, fiecare număr Fibonacci este suma celor două numere Fibonacci anterioare, rezultând secvența:
Primele 22 de numere din șir sunt: 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610 ....'''





'''Scrieti o functie care valideaza o adresa de email
gleb.tocarenco@gmail.com - valida, gleb.tocarenco@ - invalida'''

import re
email = input("Please insert your email >>> ")
def checkEmail(email):
    myPattern = re.compile(r"[a-zA-z0-9_.-]+@[a-zA-z0-9-]+\.[\w+]")
    x = myPattern.finditer(email)
    for i in x:
        if True:
            print("valid")
        elif False:
            print("not valid")

checkEmail(email)


'''Scrieti o functie care primeste la input un text cu cifre si il converteste in numar,
in caz de exceptie (este introdus o litera), afisati un mesaj de erroare si chemati
functia de convertire din nou.'''
