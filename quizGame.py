#start

#var setup

userScore = 0
questionsAnswered = 0
totalQuestions = 5

#Backround code and functions

def checkGameEnd():
    if(questionsAnswered == totalQuestions):
        print("The game is over, your final score is:", userScore, "out of", questionsAnswered)
        exit()
    

def yesOrNo(string):
    if(string == 'yes' or string == 'Yes'):
        return True
    elif(string == 'no' or string == 'No'):
        return False
    else:
        print("please respond with a 'yes' or 'no'")
        exit()

#start game code

print("Welcome to the Souhegan quiz game!")
start = input('would you like to start the game? ("yes" or "no")\n')

if(yesOrNo(start)):
    print("ok, lets start!")
else:
    print("ok then :(")
    exit()

#quiz questions

#question 1
print("the 1st qustions is: What year was Souhegan opened?")
print("A: 1999")
print("B: 2001")
print("C: 1992")
print("D: 1996")
answer1 = input('write your answer and the letter ("A", "B",ect)\n')
if(answer1 == 'c' or 'C'):
    print("correct!")
    userScore = userScore + 1
    questionsAnswered = questionsAnswered + 1
else:
    print("wrong :(")
    questionsAnswered = questionsAnswered + 1
checkGameEnd()

#question 2
print("ok, 2nd question: how many students go to souhegan?")
print("A: 1,053")
print("B: 707")
print("C: 862")
print("D: 921")
answer2 = input("what is your answer? \n")
if(answer2 == 'b' or 'B'):
    print("correct!")
    userScore = userScore + 1
    questionsAnswered = questionsAnswered + 1
else:
    print("wrong :(")
    questionsAnswered = questionsAnswered + 1
checkGameEnd()

#question 3
print("ok, 3rd question: how many AP classes are there?")
print("A: 10")
print("B: 12")
print("C: 17")
print("D: 15")
answer3 = input("what is your answer? \n")
if(answer3 == 'd' or 'D'):
    print("correct!")
    userScore = userScore + 1
    questionsAnswered = questionsAnswered + 1
else:
    print("wrong :(")
    questionsAnswered = questionsAnswered + 1
checkGameEnd()

#question 4
print("ok, 4th question: what rank is Souhegan on the best schools list?")
print("A: 3,167")
print("B: 5,257")
print("C: 2,038")
print("D: 4,109")
answer4 = input("what is your answer? \n")
if(answer4 == 'a' or 'A'):
    print("correct!")
    userScore = userScore + 1
    questionsAnswered = questionsAnswered + 1
else:
    print("wrong :(")
    questionsAnswered = questionsAnswered + 1
checkGameEnd()

#question 5
print("last one! 5th question: what subject do souhegan students test best in?")
print("A: reading")
print("B: science")
print("C: math")
print("D: history")
answer5 = input("what is your answer? \n")
if(answer5 == 'a' or 'A'):
    print("correct!")
    userScore = userScore + 1
    questionsAnswered = questionsAnswered + 1
else:
    print("wrong :(")
    questionsAnswered = questionsAnswered + 1
checkGameEnd()
