#start
#open file
try:
    file=open('english spanish word pairs - Sheet1.csv')
except:
    print('file cannot be opened')
    exit()
#data format:
#english,spanish

#adds words form csv to dictionary
spa2eng = {}
for word in file:
    word = word.strip()
    wordList = word.split(',')
    spa2eng[wordList[0]] = wordList[1]

print("This dictionary can translate most english words to spanish")
#asking user what word they would like to translate
while True:
    while True:
        word = input("what word would you like to translate?\n")
        try:
            print('you word in spanish is:', spa2eng[word])
            break
        except:
            print('word is not in dictionary, make sure its spelled correctly')
    #asking if user want to translate another word
    cont = input("would you like to translate another word?\n")
    if(cont.lower() == 'yes'):
        print("ok")
    elif(cont.lower() == 'no'):
        print('ok')
        break
    else:
        print("I'll take that as a no.")
        break
#End


