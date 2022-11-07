#start

#opens file so we can use it in code
word_file = open("scrabble_wds.txt")

#function that takes a string and returns a true if it is in the list and false if it isn't
def checkWord(word):
    word = str(word)
    #makes the word lower case so it matches with the word doc
    for line in word_file:
        if(line.find(word) != -1):   
            return True
        else:
            print(word.lower())
            return False

print('Hello! Welcome to the scrabble word checker, this program will check any word you give it and tell you if it is legal in a game of scrabble!')
word = input('please inter the word you want to check \n')

if(checkWord(word)):
    print(word, 'is totaly legal in a game of scrabble!')
else:
    print(word, 'is not a legal word in scrabble.')

while True:
    cont = input('would you like to check another word? \n')
    if(cont.lower() == 'yes'):
        word = input('Ok, what word do you want to check? \n')
    else:
        print("I'll take that as a no")
        break
    if(checkWord(word)):
        print(word, 'is totaly legal in a game of scrabble!')
    else:
        print(word, 'is not a legal word in scrabble.')