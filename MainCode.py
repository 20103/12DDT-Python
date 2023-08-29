import csv, random, math, time

from colorama import Fore, init
init(autoreset=True) #auto reset won't work for some mysterious reason

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

#Debugging, prints all available questions
"""while True:
    print(generateQuestion()[1])
"""

def runGame():
    #re/set score to 0
    playerScore = 0

    #Initial prompt & greeting.
    print(Fore.WHITE + "Hello! This is a fun trivia quiz game that will consist of varying questions and genres.")
    input(Fore.LIGHTBLACK_EX + "Press Enter to continue..." + Fore.LIGHTCYAN_EX)

    #You can consider adding a "Confirm?" prompt to the user, however this is not essential.
    #Addendum: I would have used the string split() method to eliminate excess space, however I want the user to have more freedom.
    nameInput = input(Fore.LIGHTYELLOW_EX + "Please enter a username: " + Fore.LIGHTCYAN_EX)

    #Make sure user inputs a name instead of blank space
    while nameInput.isspace() or nameInput == "":
        nameInput = input(f"{Fore.RED}You did not enter anything! {Fore.YELLOW}Please enter a username: " + Fore.LIGHTCYAN_EX)

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

        #Thanks, stack overflow!!!
        print()
        print(Fore.LIGHTYELLOW_EX + f"Genre: {topic}\n" + f"Question {i}: {question} ")
        answerInput = " ".join(str(input(Fore.LIGHTCYAN_EX + "Your Answer: ")).split()).lower()
        print()
        if answerInput == answer.lower():
            print(Fore.LIGHTGREEN_EX + "Correct!")
            playerScore += 1
        else:
            print(Fore.LIGHTRED_EX + f"Incorrect! The answer was: {answer}")
        print(desc)
        input(Fore.LIGHTBLACK_EX + "Press Enter to continue..." + Fore.LIGHTCYAN_EX)

    #Information for endScreen() function
    return(playerScore, playerName)
            
def endScreen(playerInfo):
    #For readability
    playerScore = playerInfo[0]
    playerName = playerInfo[1]

    #Endgame
    percentageScore = math.floor(playerScore / QUESTION_AMOUNT * 100)

    #get percentage by dividing playerscore with QUESTION_AMOUNT
    print()
    print(f"{Fore.YELLOW}Well done, {playerName}! You have answered all the questions.\nYour total score is: {playerScore} out of {QUESTION_AMOUNT}. This means you got {percentageScore}% of the questions correct!")
    input(Fore.LIGHTBLACK_EX + "Press Enter to continue..." + Fore.LIGHTCYAN_EX)
    print()
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
    print()
    loopInput = str(input(Fore.YELLOW + "Play again? Empty answer will be considered as no: " + Fore.LIGHTCYAN_EX))

    if loopInput.strip().lower() in ["true", "yes", "1", "y", "yeah", "sure", "ok", "okay"]:
        print(Fore.YELLOW + "Restarting game...")
        for i in range(3):
            time.sleep(0.7) #imported time library, added delay for aesthetics
            print(Fore.LIGHTBLACK_EX + ".")
        print(Fore.YELLOW + "Done!")
        input(Fore.LIGHTBLACK_EX + "Press Enter to continue...")
        print()
        print()
    else:
        break

#Final message before program terminates
print(Fore.WHITE + "Thanks for playing!")






