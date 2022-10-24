#start

#varible for keeping track of the total grades for the average
totalGrades = 0
totalGrades = float(totalGrades)
def convertGrades(double):
    #importing the totalgrades var so I can use it in the fuction (this took me a while to figure out)
    global totalGrades
    totalGrades += double
    
    #re-used if logic ladder 
    try:
        if(double <= 1.9):
            return"your grade is a NC, meaning you got no credits and you failed the class :( "
        elif(double >= 2.0 and double <= 2.6):
            return"your grade is a C, Cs are passing so not bad!"
        elif(double >= 2.7 and double <= 3.3):
            return"your grade is a B, you aren't just barely passing!"
        elif(double >= 3.4 and double <= 4.0):
            return"your grade is a A, you are the best of the best!"
        else:
            return"not a real 1.0 to 4.0 grade"
    except:
        return"function expects a float"

def askGrade():
    #try and except in a while true loop to make sure we are giving the grade conversion function a good number
    while True:
        #asking the user for their grade
        grade = input('what is the grade you need to convert? \n')
        try:
            #converting the input to a float
            grade = float(grade)
            if(grade > 4):
                print("the grading system only goes up to 4")
            else:
                break
        except:
            print("please enter a number")
    
    return grade

#start main code
print("Hello and welcome to the grade coversion program!")
while True:
    #taking the amount of students that need grades converted not just setting it at 5
    totalNumOfStudents = input('How many students need grades converted?\n')
    try:
        totalNumOfStudents=int(totalNumOfStudents)
        break
    except:
        print('the program expects a solid number, try again')

numOfStudents = totalNumOfStudents

#runs for as many times as needed by the user
for numOfStudents in range(int(numOfStudents),0,-1):
    print(convertGrades(askGrade()))
    print("There are ",numOfStudents-1, "left")

#printing the class average using 
print(totalGrades/totalNumOfStudents, " is the class average!")
print("Thank you!")
#End