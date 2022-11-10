#start

#opens file so we can use it in code
word_file = open("scrabble_wds.txt")

#function that takes a string and returns a true if it is in the list and false if it isn't
def checkWord(word):
    #resets the text doc and turns it into a list so it can be used in a loop
    word_file.seek(0)
    wordList = word_file.read()

    if(word in wordList):
        return word + ' is totaly legal in a game of scrabble!'
    else:
        return word + ' is not a legal word in scrabble.'


print('Hello! Welcome to the scrabble word checker, this program will check any word you give it and tell you if it is legal in a game of scrabble!')
#gets the word and makes it lowercase to always match the text doc
word = input('please inter the word you want to check \n')
word = word.lower()

#the function returns a string that states if the word is legal or not, I did this to make it easier to re-use the function many times 
print(checkWord(word))

while True:
    cont = input('would you like to check another word? \n')
    if(cont.lower() == 'yes'):
        word = input('Ok, what word do you want to check? \n')
        word = word.lower()
        checkWord(word)
    elif(cont.lower() == 'no'):
        print('ok')
        break
    else:
        print("I'll take that as a no")
        break

print('Thank you!')