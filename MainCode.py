import csv, random, math

from colorama import Fore, init
init(autoreset=True) #auto reset won't work for some mysterious reason

#consider adding tkinter gui if i can be bothered
#also maybe add option for multiple different answers including numerical. can be done through lists, separating them at commas etc.

with open("./questions.csv", "r", encoding='utf-8') as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=",")
    for row in reader_variable:
        data = list(reader_variable)


#CONFIG
QUESTION_AMOUNT = 10 #How many trivia questions per game

#Store current question.
questionInfo = None
usedQuestions = []

numOfQuestions = len(data) #usable with arrays

#print(Fore.LIGHTBLACK_EX + "DEBUGGING: The variable 'data' has {} trivia questions.".format(len(data)))

#Test run!

"""Note:
    0 = Trivia topic
    1 = Question
    2 = Answer
    3 = Description
"""


#This function was definitely a highlight for me. I learnt list comprehension and how useful they can be. https://www.w3schools.com/python/python_lists_comprehension.asp
def generateQuestion():
    #takes a question from data list and assigned to availableQuestions if not already present
    availableQuestions = [q for q in data if q not in usedQuestions]
    if len(availableQuestions) == 0:
        print(Fore.LIGHTRED_EX + "ERROR: NO MORE QUESTIONS AVAILABLE")
        exit()
    randomNumber = random.randint(0, len(availableQuestions) - 1)
    selectedQuestion = availableQuestions[randomNumber]
    usedQuestions.append(selectedQuestion)
    return selectedQuestion

def runGame():
    playerScore = 0

    #Initial prompt & greeting.
    print(Fore.WHITE + "Hello! This is a fun trivia quiz game that will consist of varying questions and genres.")
    input(Fore.LIGHTBLACK_EX + "Press Enter to continue..." + Fore.LIGHTCYAN_EX)

    #You can consider adding a "Confirm?" prompt to the user, however this is not essential.
    nameInput = input(Fore.LIGHTYELLOW_EX + "Please enter a username: " + Fore.LIGHTCYAN_EX)

    while nameInput.isspace() or nameInput == "":
        nameInput = input(Fore.RED + "You did not enter anything! Please enter a username: " + Fore.LIGHTCYAN_EX)

    playerName = nameInput.strip()
    print(f"{Fore.WHITE}Welcome, {playerName}!")
    input(Fore.LIGHTBLACK_EX + "Press Enter to continue..." + Fore.LIGHTCYAN_EX)

    #Main game
    print(f"{Fore.WHITE}There is a total of {QUESTION_AMOUNT} trivia questions that must be answered. You will be given a score out of {QUESTION_AMOUNT}.\nALL NUMERICAL ANSWERS ONLY ACCEPT DIGITS, DO NOT USE WORD FORM!")
    input(Fore.LIGHTBLACK_EX + "Press Enter to continue..." + Fore.LIGHTCYAN_EX)

    for i in range(1, QUESTION_AMOUNT + 1):
        #Get question & data. Store into appropriate variables.
        questionInfo = generateQuestion() #See generateQuestion() function above for more info
        topic = questionInfo[0]
        question = questionInfo[1]
        answer = questionInfo[2]
        desc = questionInfo[3]

        answerInput = str(input(Fore.LIGHTYELLOW_EX + f"Genre: {topic}\n" + f"Question {i}: {question} " + Fore.LIGHTCYAN_EX)).lower()

        if answerInput == answer.lower():
            print(Fore.LIGHTGREEN_EX + "Correct!")
            playerScore += 1
        else:
            print(Fore.LIGHTRED_EX + f"Incorrect! The answer was: {answer}")
        print(desc)
        input(Fore.LIGHTBLACK_EX + "Press Enter to continue..." + Fore.LIGHTCYAN_EX)

    return(playerScore, playerName)
            
def endScreen(playerInfo):
    #For readability
    playerScore = playerInfo[0]
    playerName = playerInfo[1]

    #Endgame
    percentageScore = math.floor(playerScore / QUESTION_AMOUNT * 100)

    #get percentage by dividing playerscore with QUESTION_AMOUNT

    print(f"{Fore.YELLOW}Well done, {playerName}! You have answered all the questions.\nYour total score is: {playerScore} out of {QUESTION_AMOUNT}. This means you got {percentageScore}% of the questions correct!")
    input(Fore.LIGHTBLACK_EX + "Press Enter to continue..." + Fore.LIGHTCYAN_EX)
    if percentageScore == 100:
        print(Fore.GREEN + "Wow, that is impressive! You answered every question correctly.")
    elif percentageScore >= 80:
        print(Fore.LIGHTGREEN_EX + "Pretty good! You got the majority of questions correct.")
    elif percentageScore >= 60:
        print(Fore.YELLOW + "Not bad! You've answered more questions correctly than incorrectly.")
    elif percentageScore >= 40:
        print(Fore.LIGHTRED_EX + "Not the best score, but there is definitely room for improvement!")
    else:
        print(Fore.RED + "Well, maybe the questions you recieved were particularly difficult! Or maybe trivia just isn't your thing. Nice try!")

#Game loop
while True:
    #Functions to run the game code
    endScreen(runGame())
    #Ask if user wants to play again
    loopInput = str(input(Fore.YELLOW + "Play again? Empty answer will be considered as no: "))

    if loopInput.strip().lower() in ["true", "yes", "1", "y", "yeah", "sure"]:
        print(Fore.YELLOW + "Restarting game...")
        input(Fore.LIGHTBLACK_EX + "Press Enter to continue...")
    else:
        break

#Final message before program terminates
print(Fore.WHITE + "Thanks for playing!")






