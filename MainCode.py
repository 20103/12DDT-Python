import pandas

questionCSV = pandas.read_csv("Questions.csv")

#Array to store the names of players (string).
playerNames = []

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
    print("Welcome, {}!".format(name))

#Main game
print("There is a total of 10 trivia questions that must be answered. You will earn points if you get the answer correct. Whoever has the most points at the end wins! ALL NUMERICAL ANSWERS ONLY ACCEPT DIGITS, DO NOT USE WORD FORM!")


