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
myList = []
import os
# from datetime import datetime
listFiles = os.listdir()

scandirContent = os.scandir(os.getcwd())
# for item in scandirContent:
#     myList.append(item.stat().st_mtime)
#     lastModified = max(myList)
# print(lastModified)

for item in scandirContent:
    for i in listFiles:
        myList.append(item.stat().st_mtime)
        lastModified = max(myList)
        print(i)
print(i, lastModified)
    # if max(listFiles, key = x):
    #     #unixTime = datetime.fromtimestamp(info.st_mtime)
    #     print(info.st_mtime)


"""Find name of last accessed filed your current working directory."""


"""1.Create new folder with name my_data_folder
2. Change path to new created folder
3. Create inside new folder one file and write there user input data about:
    Age, occupation, age, height
4. Copy content of file created in ex. 3 in new file (open file in write mode)"""
