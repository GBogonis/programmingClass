#start
#opening file
try:
    epitaph = open('epitaph.txt')
except:
    print('file cannot be opened')
    
#info format
#Name, Year of Birth, Year of Death, Epitaph

#placeholder vars
oldestAge = 0
oldestPerson = 0
for line in epitaph:
    line = str(line)
    #check for blank lines
    if(len(line) < 3):
        break
    else:
        #putting the data into a list
        bio = line.split(',')
        ageOfDeath = int(bio[2]) - int(bio[1])
       #checking who had lived the longest and replacing the vars with whoever was older
        if(oldestAge < ageOfDeath):
            oldestAge = ageOfDeath
            oldestPerson = bio[0]

#printing results
print("The person who lived the longest is", oldestPerson, 'who lived for', oldestAge, 'years')
#end