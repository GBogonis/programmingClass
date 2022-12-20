#start

#opens the file
try:
    file = open('werewolf.txt')
except:
    print('File cannot be opened')
    exit()

keyWords = ["mummy","werewolf","disguise","graveyard","cackle","cobweb","dracula","ghostly","mischief","panic"]

for line in file:
    line = line.strip()
    print(line)
    print(line.find('mummy'))
