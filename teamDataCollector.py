import statbotics

mStatbotics = statbotics.Statbotics()

numWin = 0
numLost = 0
numTie = 0
numTotal = 0

for i in range(2023,2001,-1):
    print(i)
    if(i != 2021):
        data = mStatbotics.get_team_year(138,i)
        numWin += data['full_wins']
        numLost += data['full_losses']
        numTie += data['full_ties']
        numTotal += data['full_count']

print(numWin/(numTotal-numTie))
