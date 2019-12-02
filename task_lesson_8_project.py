"""
Write a program that will generate question for guessing countrie’s capital
with 4 options of answers:

1. Read content of file countries.txt and create a dictionary with country
   as it’s key and capital as value
2. Use random module (import random) in order to get country and it’s capital,
   using same method get another 3 capitals
3. Generate question with 4 options of answer
4. Prompt user for correct answer and display after correct result
"""
import random

#Definim o clasa pentru formatarea textului in consola
class color:
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#Definim doua liste cu valorile tarilor si capitalelor din fisierul cuntries.txt
#Aceste liste vor fi utilizate pentru crearea unui dictionar = countriesDict,
#conform punctului 1. din task
countryKey = []
capitalValue = []

#Deschidem fisierul pentru citirea informatiei si pentru fiecare linie crream
#o lista = line, apoi fiecare element din lista line il atasam in liste aparte
#ce corespund tarilor si capitalilor, excludem newline char \n cu [:-1]
with open("countries.txt", "r+") as f:
    for line in f:
        line = line.split(",")
        countryKey.append(line[0])
        capitalValue.append(line[1][:-1])

#Am creat dictionarrulm tara = key, capitala = value
countriesDict = dict(zip(countryKey, capitalValue))

#Generam, cu ajutorul librariei random, o lista cu 4 elemente
# luate la intimplare din Lista capitalelor creata mai sus
randomCapital = random.sample(capitalValue, k = 4)

print(color.BOLD + "\nPlay a game by guessing the countries' capitals.\n"\
      + color.END)

#Pentru a crea un quiz(test grila), definim inca doua liste ajutatoare
#Aceste liste reprezinta optiunile de raspuns
answerOptions = ["A", "B", "C", "D"]
answerCapital = []

#Definim o functie care executa logica quiz-ului
def guessCapital():
    #Iteram prin dictionarul ce contine toate elementele din fisier,
    #luam o valoare(capitala) la itimplare pentru a fi ghicita, egalam
    #acea valoare cu al doilea element (putea fi luat orisicare 0,1,2 sau 3)
    #din lista generata cu functia random
    for key, value in countriesDict.items():
        if value == randomCapital[1]:
            #Mestecam valorile din lista, in caz constrar varianta corecta
            # se va afla mereu pe pozitia doi
            random.shuffle(randomCapital)

            #Afisam tara si variantele de raspuns
            print("What is the capital of", color.UNDERLINE + f"{key}"\
                 + color.END, "please choose from:" )
            print("\n---------------------------"\
                 f"\n A) {randomCapital[0]}\n B) {randomCapital[1]}"\
                 f"\n C) {randomCapital[2]}\n D) {randomCapital[3]}"\
                  "\n----------------------------")
            #Dupa shuffle, atasam fiecare varianta de raspuns in lista noua
            #astfel incit sa corespunda ordinii afisate 0,1,2 si 3
            answerCapital.append(randomCapital[0])
            answerCapital.append(randomCapital[1])
            answerCapital.append(randomCapital[2])
            answerCapital.append(randomCapital[3])
            #Creem dictionar nou in care atasam variantele de raspuns
            optionsDictionary = dict(zip(answerOptions, randomCapital))
            #Curatim lista cu raspunsuri dupa ce am creat dictionarul in caz
            #contrar de fiecare data cind va fi chemata functia guessCapital()
            #lista se va extinde adugind aceleasi elemente din nou
            answerCapital.clear()
            #Utilizatorul insereaza raspunsul sau, convertim raspunsul in
            #upper case, ca sa nu fie case sensitive
            userAnswer = input(f"Your answer is: ")
            userAnswer = userAnswer.upper()
            #Dam posibilitate utilizatorului sa introduca raspunsul sau in doua
            #moduri, fie alegind A,B,C,D sau sa tapeze denumirea capitalei
            if userAnswer == countriesDict.get(key)\
               or optionsDictionary.get(userAnswer) == countriesDict.get(key):
                print(color.GREEN + "\nCongrats! Your answer is correct.\n"
                      + color.END)
                print(color.BLUE + "Play more or type '1' to quit the game\n"
                      + color.END)
                guessCapital()
            #Daca raspunsul e corect, are doua optiuni: sa continue jocul sau
            #sa iasa tapind "1"
            elif userAnswer == "1":
                print(color.BLUE + "\nBye! See you again on game" + color.END)
                exit()
            #Daca raspunsul e gresit, afisam raspunsul corect si il rugam
            #sa incerce din nou(iarasi chemam functia guessCapital())
            else:
                print("\nRight answer is", color.RED + f"{countriesDict.get(key)}"
                      + color.END)
                print(color.RED + "\nDon't give up and try again.\n"
                      + color.END)
                guessCapital()

guessCapital()
