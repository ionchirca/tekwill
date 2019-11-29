"""Calculate sum of size all .py files in your working directory. Convert in in
MegaBytes."""

# import os
# #Scaneaza fisierele din directoria curenta pentru a afla marimea, uid,
# # timestamps ale fisierelor
# scandirContent = os.scandir(os.getcwd())
# sum = 0
# #Pentru toate fisierele din directoria curenta (listdir() method)
# for item in os.listdir():
#     #Pentru toate caracterele din denumirea de fisiere din directorie
#     for char in scandirContent:
#         if item.split('.'):
#             if item[-2:] == 'py':
#                 info = char.stat()
#                 sum = sum + info.st_size
# print("The total size of .py files in my current working directory is %sMB"\
#       % (round(sum / 1024, 2)))



"""Find name of last modified file in your current working directory."""
"""Find name of last accessed filed your current working directory."""

# import os
# from datetime import datetime #pentru conversia unix time readable datetime
#
# #Creem 3 liste pentru a salva info ca nume de fisiere, data accesarii si modificarii
# nameofFiles = []
# modifiedFiles = []
# accessedFiles = []
#
# #Listam fisierele din directoria curenta, similar cu "ls" in linux
# #Scanam fisierele pentru a culege info despre ele, cind au fost modificate, cine etc
# listFiles = os.listdir()
# scandirContent = os.scandir(os.getcwd())
#
# #Atasam fiecare fisier si info despre el in listele create mai sus
# for file in listFiles:
#     nameofFiles.append(file)
#
# for item in scandirContent:
#     modifiedFiles.append(item.stat().st_mtime)
#     accessedFiles.append(item.stat().st_atime)
#
# #Creem dictionare cu perechile key = nume fisier, value = data modificarii, accesarii
# myDict = dict(zip(nameofFiles, modifiedFiles))
# myDict2 = dict(zip(nameofFiles, accessedFiles))
#
# #Pentru fiecare item din perechea key, value, daca valoarea corespunde
# #cu valoarea maxima din lista creata atunci afiseaza rezultatul
# for fileName, fileModified in myDict.items():
#     if fileModified == max(modifiedFiles):
#         print(f"The name of last modified file is {fileName}, it was modified"\
#               f" on {datetime.fromtimestamp(item.stat().st_mtime)}" )
#
# for fileName, fileAccessed in myDict2.items():
#     if fileAccessed == max(accessedFiles):
#         print(f"The name of last accessed file is {fileName}, it was accessed"\
#               f" on {datetime.fromtimestamp(item.stat().st_atime)}" )

"""
1.Create new folder with name my_data_folder
2. Change path to new created folder
3. Create inside new folder one file and write there user input data about:
    Age, occupation, age, height
4. Copy content of file created in ex. 3 in new file (open file in write mode)"""


""" Write a program that will count number of lines in a file """
""" Write a program that will count frequency of a word in a file """

# with open("task_lesson_8.py", "r") as f:
#     #Deschide si citeste fiecare linie din fisier de la pozitia 0
#     for line in f:
#         f.seek(0)
#         line = f.read()
#     #Calculeaza numarul de newline characters, deoarece fiecare line incepe cu el
#     print("Number of lines in file task_lesson_8.py = %s" % line.count("\n"))
#     f.seek(0)
#     #Dupa ultima operatie, muta cursorul de la inceput si calculeaza
#     #numarul de aparitii a cuvintului test_word pe fiecare linie
#     if "test_word" in line:
#         value = line.count("test_word")
#     print("Number of appearences of 'test_word' in file task_lesson_8.py = %s" % value)


""" Write a program that will append new content to the end of a file. """
""" Write a program that will remove newline character from a file. """


# with open("test_file_task_8.txt", "a+") as f:
#     for num in range(1, 6):
#         #Genereaza random text in fisierul deschis si muta cursorul la inceput
#         # pentru citirea continutului, in caz contrar nimic nu va fi afisat
#         f.write("This is line number %s\n" % num)
#         f.seek(0)
#     print("\nBellow is the content of new created file")
#     print("   -----------------------------\n")
#     print(f.read())
#     print("   -----------------------------")
#
# with open("test_file_task_8.txt", "r+") as f:
#     #Citeste continutul fisierului si shimbai formatul/type in string
#     line = str(f.read())
#     f.seek(0)
#     # Inlocuieste orice 'newline' char cu un 'space' char
#     f.write(line.replace("\n", " "))
#     f.seek(0)
#     print("\nBellow is the content of the file without newline character\n")
#     print("   -----------------------------\n")
#     print(f.read())
