#start

#opening the test file with the names and grades
gradeFile = open("grades.txt")

#re-used grade conversion function from past projects
def convertGrades(grade):
    try:
        if(grade <= 1.9):
            return"your grade is a NC, meaning you got no credits and you failed the class :( "
        elif(grade >= 2.0 and grade <= 2.6):
            return"your grade is a C, Cs are passing so not bad!"
        elif(grade >= 2.7 and grade <= 3.3):
            return"your grade is a B, you aren't just barely passing!"
        elif(grade >= 3.4 and grade <= 4.0):
            return"your grade is a A, you are the best of the best!"
        else:
            return"not a real 1.0 to 4.0 grade"
    except:
        return"function expects a float"

#loop to print the names and grades by trying to convert the line into a float then into a letter grade but if its not possible(if its a name) it will just print normal. 

for line in gradeFile:
    try:
        line = float(line)
        print(convertGrades(line))
    except:
        print(line)
print('End')
