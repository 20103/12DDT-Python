import csv, random, colorama

from colorama import Fore
colorama.init(autoreset=True)

#consider adding tkinter gui if i can be bothered

with open("./questions.csv", "r", encoding='utf-8') as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=",")
    for row in reader_variable:
        data = list(reader_variable)

#CONFIG
QUESTION_AMOUNT = 10 #How many trivia questions per game

#Store current question.
questionInfo = None
usedQuestions = []

playerScore = 0

numOfQuestions = len(data) #usable with arrays

#print("DEBUGGING: The variable 'data' has {} trivia questions.".format(len(data)))

#Test run!

"""Note:
    0 = Trivia topic
    1 = Question
    2 = Answer
    3 = Description
"""


#This function was definitely a highlight for me. I learnt list comprehension and how useful they can be. https://www.w3schools.com/python/python_lists_comprehension.asp
def generateQuestion():
    availableQuestions = [q for q in data if q not in usedQuestions]
    if len(availableQuestions) == 0:
        print("ERROR: NO MORE QUESTIONS AVAILABLE")
        exit()
    randomNumber = random.randint(0, len(availableQuestions) - 1)
    selectedQuestion = availableQuestions[randomNumber]
    usedQuestions.append(selectedQuestion)
    return selectedQuestion


#Initial prompt & greeting.
print("Hello! This is a fun trivia quiz game that will consist of varying questions and genres.")

#You can consider adding a "Confirm?" prompt to the user, however this is not essential.
nameInput = input("Please enter a username: ")

while nameInput.isspace():
    nameInput = input("You did not enter anything! Please enter a username: ")

playerName = nameInput.strip()
print(f"Welcome, {playerName}!")

#Main game
print(f"There is a total of {QUESTION_AMOUNT} trivia questions that must be answered. You will be given a score out of {QUESTION_AMOUNT}.\n ALL NUMERICAL ANSWERS ONLY ACCEPT DIGITS, DO NOT USE WORD FORM!")

for i in range(1, QUESTION_AMOUNT + 1):
    #Get question & data. Store into appropriate variables.
    questionInfo = generateQuestion()
    topic = questionInfo[0]
    question = questionInfo[1]
    answer = questionInfo[2].lower()
    desc = questionInfo[3]

    answerInput = str(input(Fore.YELLOW + f"Genre: {topic}\n" + f"Question {i}: {question} ")).lower()

    if answerInput == answer:
        print(Fore.GREEN + "Correct!")
        playerScore += 1
    else:
        print(Fore.RED + f"Incorrect! The answer was: {answer}")
    print(desc)
        
#Endgame
percentageScore = playerScore / QUESTION_AMOUNT * 100

print(percentageScore)

#get percentage by dividing playerscore with QUESTION_AMOUNT

print(f"You have answered all the questions. \n Your total score is: {playerScore} out of {QUESTION_AMOUNT}")
if percentageScore == 100:
    print("Wow, that is impressive! You answered every question correctly.")
elif percentageScore >= 80:
    print("Pretty good! You got the majority of questions correct.")
elif percentageScore >= 60:
    print("Not bad! You've answered more questions correctly than incorrectly.")
elif percentageScore >= 40:
    print("Not the best score, but there is definitely room for improvement!")
else:
    print("Well, maybe the questions you recieved were particularly difficult! Or maybe trivia just isn't your thing. Nice try!")







