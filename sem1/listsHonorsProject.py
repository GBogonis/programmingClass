#start
#open file
poemFile = open("Cambridgeladies.txt")
poemList = poemFile.readlines()

#vars for holding the shortest and longest words
longestWord = ''
shortestWord = '                                      '

#loop for every line in the poem
for line in poemList:
    #sets the length for the words every loop so its always up to date
    longestWordLen = len(longestWord)
    shortestWordLen = len(shortestWord)

    line = line.rstrip()
    print(line)
    #split the line up into a list and sorts it 
    lineList = line.split(' ')
    lineList.sort()

    #loop for every word in the sorted line list
    for word in lineList:

        word = word.strip()
        #compairs the words to the current shortest and longest words saved
        if(len(word) > longestWordLen):
            longestWord = word
        if(len(word) < shortestWordLen and len(word) >= 1):
            shortestWord = word
    #prints the sorted line list as a string
    print(' '.join(lineList))

#print the longest and shortest words that were found.
print("the longest word is", longestWord)
print("the shortest word is", shortestWord)
#end