#start

#opens the file
try:
    file = open('werewolf.txt')
except:
    print('File cannot be opened')
    exit()

keyWords = ["mummy","werewolf","disguise","graveyard","cackle","cobweb","dracula","ghostly","mischief","panic"]

for line in file:
    lineStrip = line.strip()
    print(lineStrip)
    if(lineStrip.find('m u m m y') == -1):
        print(-1)
    else:
        print(lineStrip[lineStrip.find('m u mm y'): lineStrip.find('m u m m y')+ len('m u m m y')])
