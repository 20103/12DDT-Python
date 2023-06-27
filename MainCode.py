import csv, random

with open("./questions.csv", "r", encoding='utf-8') as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=",")
    for row in reader_variable:
        data = list(reader_variable)

#CONFIG
QUESTION_AMOUNT = 10 #How many trivia questions per game

#Store current question.
questionInfo = None

#Array to store the names of players (string).
playerNames = []
playerScores = []

numOfQuestions = len(data) #usable with arrays

#print("DEBUGGING: The variable 'data' has {} trivia questions.".format(len(data)))

#Test run!

"""Note:
    0 = Trivia topic
    1 = Question
    2 = Answer
    3 = Description
"""

def generateQuestion():
    randomNumber = random.randint(1, numOfQuestions - 1) #Confused me for a while, the questions start at 1 and end at 19 (index).
    questionList = data[randomNumber]
    questionArray = []
    for i in range(len(questionList)):
        questionArray.append(questionList[i])
        i += 1
    return questionArray


#Initial prompt & greeting.
print("Hello! This is a fun trivia quiz game that will consist of varying questions and genres. There is a maximum of 4 players.")

numOfPlayers = int(input("Please type how many people will be playing (e.g. 2): ").strip())

#Ask user again if the input is above 4 or below 1.
while numOfPlayers > 4 or numOfPlayers < 1:
    numOfPlayers = int(input("Sorry, but that is not a valid answer! Please type how many people will be playing (e.g. 2): "))

#You can consider adding a "Confirm?" prompt to the user, however this is not essential.
for i in range(numOfPlayers):
    name = input("Please enter a name Player {}: ".format(i+1)).strip()
    playerNames.append(name)
    playerScores.append(0)
    print("Welcome, {}!".format(name))

#Main game

#I use both "f" and "format". Why? I don't know.
print(f"There is a total of {QUESTION_AMOUNT} trivia questions that must be answered. You will earn points if you get the answer correct. Whoever has the most points at the end wins! ALL NUMERICAL ANSWERS ONLY ACCEPT DIGITS, DO NOT USE WORD FORM!")

for i in range(1, QUESTION_AMOUNT):
    #Get question & data. Store into appropriate variables.
    questionInfo = generateQuestion()
    topic = questionInfo[0]
    question = questionInfo[1]
    answer = questionInfo[2]
    desc = questionInfo[3]

    answerInput = str(input(f"Question {i}: {question} "))







