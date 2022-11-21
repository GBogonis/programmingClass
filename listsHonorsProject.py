#start
poemFile = open("Cambridgeladies.txt")
poemList = poemFile.readlines()
longestWord = ''
shortestWord = '                                      '
for line in poemList:
    longestWordLen = len(longestWord)
    shortestWordLen = len(shortestWord)
    line = line.rstrip()
    if line == "\n":
        print("yep")
    print(line)
    lineList = line.split(' ')
    lineList.sort()
    for word in lineList:
        #
        # print(word)
        # word = word.strip()
        if(len(word) > longestWordLen):
            longestWord = word
        if(len(word) < shortestWordLen and len(word) >= 1):
            shortestWord = word
    print(' '.join(lineList))
print("the longest word is", longestWord)
print("the shortest word is", '!'+shortestWord+'!')
    