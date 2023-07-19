import csv, random

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

#Array to store the names of players (string).
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
print("Hello! This is a fun trivia quiz game that will consist of varying questions and genres. There is a maximum of 4 players.")

#You can consider adding a "Confirm?" prompt to the user, however this is not essential.
nameInput = input("Please enter a username: ")

while nameInput.isspace():
    playerName = input("You did not enter anything! Please enter a username: ")

playerName = nameInput.strip()
print(f"Welcome, {playerName}!")

#Main game
print(f"There is a total of {QUESTION_AMOUNT} trivia questions that must be answered. You will earn points if you get the answer correct. Whoever has the most points at the end wins! ALL NUMERICAL ANSWERS ONLY ACCEPT DIGITS, DO NOT USE WORD FORM!")

for i in range(1, QUESTION_AMOUNT + 1):
    #Get question & data. Store into appropriate variables.
    questionInfo = generateQuestion()
    topic = questionInfo[0]
    question = questionInfo[1]
    answer = questionInfo[2]
    desc = questionInfo[3]

    answerInput = str(input(f"Question {i}: {question} ")).lower()

    if answerInput == answer:
        print("Correct!")
    else:
        print(f"Incorrect! The answer was: {answer}")
    print(desc)
        

    







