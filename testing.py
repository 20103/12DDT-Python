playerScore = 13
QUESTION_AMOUNT = 23

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