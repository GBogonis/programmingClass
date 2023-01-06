#start

#opens the file
try:
    file = open('werewolf.txt')
except:
    print('File cannot be opened')
    exit()

#list of words to find in the wordsearch
keyWords = ["mummy","werewolf","disguise","graveyard","cackle","cobweb","dracula","ghostly","mischief","panic"]

for line in file:
    
    #gets rid of all the spaces in the line
    rawLine = line.split(' ')
    formatedLine = ''.join(rawLine)
    
    for word in keyWords:
        #looks for the words in the lines and makes them with all uppercase and prints out the line
        if(formatedLine.find(word) != -1):
            finishedline = formatedLine.replace(word,word.upper())
            print('found:', word, 'in', finishedline)
        
#end