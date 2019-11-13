### __1__
""" Scrieti un program care sa afiseze toti divizorii unui numar intreg. """

# number = input("Please type an integer number >>> ")
# my_list = []
# number = abs(int(number))
# for i in range(1,int(number) + 1):
#     if (int(number) % int(i) == 0):
#         my_list.append(i)
# print(my_list)

### __2__
""" Calculati suma toturor numerelor intre 1000 si 2300 care se impart fara rest
la 5 si 7. """

#print(sum(num for num in range(1000, 2300) if (num %5 == 0 and num %7 == 0)))

### __3__
""" Scrieti un program care sa primeasca la input un numar N intreg si sa
creeze un dictionar care contine numer mai mici sau egale decit N si N*2.
Ex(4 - > {1:1, 2: 4, 3: 9, 4: 16}) """

# number = input("Input a integer number >>> ")
# key_list = []
# values_list = []
# for i in range(1,int(number) + 1):
#     key_list.append(i)
#     values_list.append(i*2)
#     dictionary = dict(zip(key_list, values_list))
# print(dictionary)


### __4__
""" Scrieti un program care sa calculeze numarul de litere si cifre din un
 text."""


# text = (input("Please input some text >>> "))
# num_of_digits = []
# num_of_letters = []
# for item in text:
#     if item.isdigit():
#         num_of_digits.append(item)
#     elif item.isalpha():
#         num_of_letters.append(item)
# print("Number of digits are %s " % len(num_of_digits))
# print("Number of letters are %s " % len(num_of_letters))



### __5__
""" Scrieti un program care verifica daca o parola introdusa de utilizator este
securizata
● Lungimea minima 6 caractere
● Cotine cel putin 1 litera in intervalul [a-z]
● Cotine cel putin 1 litera in intervalul [A-Z]
● Cotine cel putin 1 cifra
● Contine cel putin un caracter special [!, /, #]
● Nu contine caractere interzire [@, ‘, {, }] """

# import re
# def check_passwd():
#     passwd = (input("Please submit a password >>> "))
#     if len(passwd) < 6:
#         print("\033[91m {}\033[00m" .format("""
#               Password should be at least 6 characters long;
#               to contain at least one upper, one lower case, one digit
#               and one special character !, / or #\n"""))
#         check_passwd()
#     elif (not re.search("[a-z]", passwd) or\
#          not re.search("[A-Z]", passwd) or\
#          not re.search("[0-9]", passwd) or\
#          not re.search("[!#/]", passwd) or\
#          re.search("[@\'{}]", passwd)):
#          print("\033[91m {}\033[00m" .format("""
#                Password should be at least 6 characters long;
#                to contain at least one upper, one lower case, one digit
#                and one special character !, / or #\n"""))
#          check_passwd()
#     else:
#         print("You've entered a valid password")
#
# check_passwd()


### __6__
""" Scrieti un program care calculeaza frecventa cu care apare un cuvint intr-o
propozitie. """


import re
sentence = input("Input some random text >>> ")
def word_freq():
    list_of_words = sentence.split(" ")
    for item in list_of_words:
        values = list(str(list_of_words.count(item)))
        print(values)
        item += 1
        for key in range(len(list_of_words)):
            keys = [key]
            dictionary = dict(zip(list_of_words, values))
    print(dictionary)


word_freq()


### __7__
""" Scrieti un program care sa elimine cuvinte duplicate dintr-o propozitie."""

# import re
# sentence = input("Input some random text that will contain some duplicate words >>> ")
