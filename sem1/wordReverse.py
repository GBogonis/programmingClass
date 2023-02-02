#start

#function to reverse words
def reverse(word):
    #makes the string into a list, reverses the list, and turns it back into a string and returns that
    letterList = []
    letterList.extend(word)
    letterList.reverse()
    return ''.join(letterList)

print("Hello! this program is made to reverse any word you give it")

#loop that lets the users reverse as many words as they want
while True:
    word = input("What word would you like to reverse?\n")
    print('The word inputted was',word,'that word reversed is:',reverse(word))
    cont = input("whould you like to reverse another word?\n")
    if(cont == 'yes' or cont == 'Yes'):
        print("ok")
    elif(cont == 'no' or cont == 'No'):
        print('ok')
        break
    else:
        print("I'll take that as a no.")
        break
    
print("Thank you!")