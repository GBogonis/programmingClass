#start

#the 2 main strings this program is based on 
#note: I removed a space at the end of the first quote, this might affect some of the results
quote1 = "No no he's not dead, he's restin'! Remarkable bird, the Norwegian Blue, idn'it, ay? Beautiful plumage!"

quote2 = "I took the liberty of examining that parrot when I got it home, and I discovered the only reason that it had been sitting on its perch in the first place was that it had been NAILED there."

count1 = 0
for letter in quote1:
    if letter == 'e':
        count1 = count1 + 1
print("There are ",count1, '"e"s in quote 1')

count2 = 0
for letter in quote2:
    if letter == 'e':
        count2 = count2 + 1
print("There are ",count2, '"e"s in quote 2')