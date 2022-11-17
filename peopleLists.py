#start
peopleFile = open("peoples.csv")

def merryFestivus():
    peopleFile.seek(0)
    for item in peopleFile:
        item = item.rstrip()
        itemList = item.split(',')
        fullName = itemList[1] + ' ' + itemList[0]
        print("Have a merry Festivus", fullName + "!")

def sortNames():
    peopleFile.seek(0)
    listOfLists = []
    for item in peopleFile:
        item = item.rstrip()
        itemList = item.split(',')
        listOfLists.append(itemList)
    listOfLists.sort()
    for stuff in listOfLists:
        print(stuff[1] + ' ' + stuff[0])
    

sortNames()



    
        




