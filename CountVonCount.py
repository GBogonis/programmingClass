#start

#opens the file
try:
    file = open('Abe_Lincoln_speech.txt')
except:
    print('File cannot be opened')
    exit()

#making the dictionary
counts = dict()

#loop for adding each word and any other occurrences of that word to the dictionary (I totally didn't steal this)
for line in file:
    words = line.split()
    for word in words:
        if word not in counts:
            #adding new word
            counts[word] = 1
        else:
            #adding 1 onto the number of occurrences that word has
            counts[word] += 1

#using the max() function to find the word with the most occurrences
mostCommonWord = max(counts, key=counts.get)
occurrences = counts.get(mostCommonWord)

#prints the results
print('The most common word in this speech is: "'+mostCommonWord+'"','with',occurrences,"occurrences")
