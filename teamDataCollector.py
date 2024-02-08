import statbotics

mStatbotics = statbotics.Statbotics()

class team:
    def __init__(self, teamNum):
        self.number = teamNum
        self.wins = 0
        self.lost = 0
        self.tie = 0
        self.total = 0
        
    def getTeamNum(self):
        return self.number
    
    def addWin(self,gamesWon):
        self.wins += gamesWon
        
    def addLost(self,gamesLost):
        self.lost += gamesLost
        
    def addTie(self,gamesTie):
        self.tie += gamesTie
        
    def addTotal(self,gamesTotal):
        self.total += gamesTotal
        
    def getWinRate(self):
        if(self.total == 0):
            return 0
        return (self.wins/(self.total-self.tie))
    
    def getRookieYear(self):
        try:
            return mStatbotics.get_team(int(self.number))['rookie_year']
        except:
            return "no rookie year"



teamsFile = open("teams.txt")
teams = []


for i in teamsFile:
    teams.append(team(i))


for i in range(2023,2001,-1):
    
    if(i != 2021):
        for t in teams:  
            try:
                print(i)
                print(t.number)
                if(int(t.getRookieYear()) < i):
                    data = mStatbotics.get_team_year(int(t.number),i)
                    t.addWin(data['full_wins'])
                    t.addLost(data['full_losses']) 
                    t.addTie(data['full_ties'])
                    t.addTotal(data['full_count'])
            except:
                print("no data")
                continue

for i in teams:
    
    print(str(i.number) + " has a winrate of " + str(i.getWinRate()))
