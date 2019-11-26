"""Scrieti un program care sa calculeze suma numerelor pare dintr-o lista, folositi
functiile reduce / filter"""
# from functools import reduce
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# newList = reduce(lambda x, y: x + y, (filter(lambda x: x % 2 == 0, myList)))
# print(newList)

"""Scrieti un functie generator care sa lucreze ca functia enumerate (yield)"""

# import string
# numbers = [num for num in range(30)]
# letters = [char for char in string.ascii_lowercase]
# def zipGenerator():
#     yield list(zip(numbers, letters))
#
# for pair in zipGenerator():
#     print(pair)

"""Scrieti un program care transforma o lista cu elemente compuse intr-o lista
simpla ( [1, [2, 3, [4, 5]]] -> [1,2,3,4,5] )"""
# myList = []
#
# a = iter([1, [2, 3, [4, 5]]])
# myList.append(next(a))
# b = iter(next(a))
# myList.append(next(b))
# myList.append(next(b))
# c = iter(next(b))
# myList.append(next(c))
# myList.append(next(c))
# print(myList)

# myList = [[1], [2, 3], [4, 5]]
# x = sum(myList, [])
# print(x)

# from functools import reduce
# myList = [[1], [2, 3], [4, 5]]
# flatList = reduce(lambda z, y :z + y, myList)
# print(flatList)

import itertools
list_of_lists = [1, [2, 3, [4, 5]]]
if item isdigit) in list_of_lists
chain = list(itertools.chain(*list_of_lists))
print(chain)

"""Scrieti o functie care primeste 2 parametri, 1 functie si o lista, rezultatul
returnat trebuie sa fie lista modificata de fuctie:

In: def my_fync(lambda x: x*x, [1, 2, [3, 4, [5]]])
Out: [1, 4, [9, 16, [25]]]"""

# myFunc = lambda x: x * x
# myList = [num for num in range(10)]
# def listFunc(*args):
#     newList = []
#     for item in myList:
#         item = myFunc(int(item))
#         newList.append(item)
#     return newList
#
# print(listFunc(myFunc, myList))
