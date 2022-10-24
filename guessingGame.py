#start

#setup stuff
import random

answer = random.randint(1,20)
answer = int(answer)

#function for seeing if the users guess was right and returning true if it is right and flase if its wrong
def testGuess(guess):
    if(guess == answer):
        print("you got it!")
        return True
    elif(int(guess) > answer):
        print("you guessed too high")
        return False
    elif(int(guess) < answer):
        print("you guessed too low")
        return False

def guessingGame():
    global answer
    #in the case that this isn't the users first play through of the game, the answer needs to be re-rolled
    answer = random.randint(1,20)
    numOfGuesses = 5
    print(answer)
    #loop that runs for as many guesses as the user has
    for numOfGuesses in range(int(numOfGuesses),0,-1):
        guess = input("what is your guess? \n")
        #try and except to stop the "testGuess" fucntion from getting a bad input 
        try:
            if(testGuess(int(guess)) == True):
                #if statement that ensures propber grammer (so it doesn't say "you had 1 guesses left")
                if(numOfGuesses-1 == 1):
                    print("You had ",numOfGuesses-1," guess left, goodjob!" )
                else:
                    print("You had ",numOfGuesses-1," guesses left, goodjob!")
                break
            else:
                print("You have ", numOfGuesses-1, " left")
        except:
            print("You are supposed to type a whole number, you lose a guess for that.")
            print("You have ", numOfGuesses-1, " left")

#start code
print("Hello and welcome to the guessing game!")
print("In this game you will have 5 attempts to find the random number between 1 and 20")

#intro to the game
while True:
    begin = input('Are you ready to begin? (yes or no)\n')
    if (begin == "yes" or begin == "Yes"):
        print("Ok let's go!")
        break
    elif(begin == 'no' or begin == "No"):
        print("well too bad")
        break
    else:
        print('A "yes" or "no" would work the best.')

guessingGame()

#asking the user if they want to play again, this can go on forever
while True:
    playAgain = input('would you like to play again?\n')
    if(playAgain == "yes" or playAgain == "Yes"):
        print("ok!")
        guessingGame()
    else:
        print("I will take that as a no.")
        break

print("Thank you for playing!")
