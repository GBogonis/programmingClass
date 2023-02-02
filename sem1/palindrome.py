#start

#reverse function to reverse words
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

print("Hello this program is designed to turn any string of text into a palindrome, give it a try!")

#loop to let user go through as many words as they want
while True:
    word = input('What word(s) do you want to be turned into a palindrome?\n')
    palindrome = word + reverse(word)
    print('The palindrome form is:'+palindrome)
    #asking if user want to generate another palindrome
    cont = input("would you like to generate another palindrome?\n")
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