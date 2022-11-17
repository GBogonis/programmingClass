#start
peopleFile = open("peoples.csv")
#data format
#last name, first name, weight, hight, hobby, food

#function 1 to tell everyone to have a merry festivus(off-brand Christmas)
def merryFestivus():
    peopleFile.seek(0)
    #in each function there is a loop that takes each line and splits it up into a list to use
    for item in peopleFile:
        item = item.rstrip()
        itemList = item.split(',')
        fullName = itemList[1] + ' ' + itemList[0]
        print("Have a merry Festivus", fullName + "!")

#function 2 to sort the names of people in alphabetical order by last name
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
    
#function 3 to tell people who like hiking that i like it too and people that like tofu that they're wrong
def hikingHobby():
    peopleFile.seek(0)

    for item in peopleFile:
        item = item.rstrip()
        itemList = item.split(',')
        if(itemList[4] == 'Hiking'):
            print('Hey,', itemList[1], 'I like hiking too!')
        if(itemList[5] == 'Tofu'):
            print(itemList[1] + ", bacon is better and you should feel bad about liking tofu")

merryFestivus()
sortNames()
hikingHobby()