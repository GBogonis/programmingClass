#start

#function setup
def convertGrades(double):
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

#asking the user for their grade
gradeInput = input('Hello! to convert your grade first we need to know your grade! \n')

#converting the input to a float
try:
    grade = float(gradeInput)
except:
    print("please enter a number next time")
    exit()

print(convertGrades(grade))



print("Thank you!")
#End