#start

#asking the user for their grade and converting the input to a float
try:
    grade = input('Hello! to convert your grade first we need to know your grade! \n')
    grade = float(grade)
except:
    #if they input something wrong then the except catches it
    print("please enter a number next time")
    exit()


#big IF ladder for converting the grade

if(float(grade) <= 1.9):
    print("your grade is a NC, meaning you got no credits and you failed the class :( ")
elif(float(grade) >= 2.0 and grade <= 2.6):
    print("your grade is a C, Cs are passing so not bad!")
elif(float(grade) >= 2.7 and grade <= 3.3):
    print("your grade is a B, you aren't just barely passing!")
elif(float(grade) >= 3.4 and grade <= 4.0):
    print("your grade is a A, you are the best of the best!")
else:
    print("not a real 1.0 to 4.0 grade")

print("Thank you!")
#End