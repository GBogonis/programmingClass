import math

file = open("winRates.txt")

for line in file:
    numbers = line.split(' has a winrate of ')
    numbers[1] = round(float(numbers[1])*100)
    print(str(numbers[0]) + " has a winrate of " + str(numbers[1]) + "%")
    