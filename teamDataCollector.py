import statbotics

mStatbotics = statbotics.Statbotics()

class team:
    def __init__(self, teamNum):
        self.number = teamNum
        self.wins = 0
        self.lost = 0
        self.tie = 0
        self.total = 0
        self.rookieYear = mStatbotics.get_team(int(self.number))['rookie_year']
      
    def getWinRate(self):
        if(self.total == 0):
            return 0
        return (self.wins/(self.total-self.tie))
    
    def setData(self):
        for i in range(2023,2001,-1): 
            if(i != 2021):
                if(int(self.rookieYear) <= i):
                    data = mStatbotics.get_team_year(int(self.number),i)
                    self.wins += data["full_wins"]
                    self.lost += data["full_losses"]
                    self.tie += data["full_ties"]
                    self.total += data["full_count"]



teamsFile = open("teams.txt")
teams = []

for i in teamsFile:
    teams.append(team(i))

