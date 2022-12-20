#start

english2klingon = dict()

#big dictionary
english2klingon = {'hello':'nuqneH',"bye":"qonwI'",'one':"wa'",'two':"cha'",'three':"Wej",'like':"parHa'",'have':'ghaj','me':'cho','you':'SoH','name':'pong','computer':"De'wI'",'programming':'ghun','robot':'qoq','school':'DuSaQ','teacher':"ghojmoHwI'"}

#list of the english words
english = ['hello','bye','one','two','three','like','have','me','you','name','computer','programming','robot','school','teacher']

#function to see if a word is in the list
def wordInList(word):
    for item in english:
        if(word == item):
            return True
    return False

print('Hello! this program is made to translate 15 words from english to klingon')

#while true loop so user can translate as many words as they want
while True:
    print('the words are:')
    for word in english:
        print(word)
    
    #check if the input is usable
    while True:
        word = input('please type the word you want to translate\n')
        if(wordInList(word.lower())):
            break
        else:
            print('that word is not in the dictionary')

    #printing results
    print(word,"in klingon is",english2klingon[word.lower()])

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

print('Thank you!')
#end