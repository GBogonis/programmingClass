#start

#open the name file and making a new output file
nameFile = open("namesClass.txt")
outputFile = open("namesClassEmailOutput.txt", "w") 

for line in nameFile:
    line = str(line)

    #spliting the line into the first and last name
    commaPos = line.find(',')
    last = line[:commaPos]
    first = line[commaPos+2:len(line)-1]
    
    #turning the names into emails and writing them into a new file
    email = first + '.' + last + '@student39.org'
    outputFile.write(email)
    outputFile.write('\n')
print('Done!')




