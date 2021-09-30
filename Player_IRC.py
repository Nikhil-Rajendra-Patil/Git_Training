class Player:
  def __init__(self,playerName,playerCountry,playerAge,noOfMatches,noOfRuns,noOfWickets):
    self.playerName  = playerName 
    self.playerCountry  = playerCountry 
    self.playerAge  = playerAge 
    self.noOfMatches = noOfMatches 
    self.noOfRuns  = noOfRuns 
    self.noOfWickets = noOfWickets 

class Team:
  def getMinRuns(self,List):
    minName = ''
    minRuns = 99999
    minCountry = ''
    for i in range(len(List)):
      if List[i].noOfRuns  < minRuns:
        minRuns = List[i].noOfRuns 
        minName = List [i].playerName 
        minCountry = List[i].playerCountry 
    print(minName)
    print(minRuns)
    print(minCountry)
 
  def getMaxWickets(self,List):
    maxName = ''
    maxWicket = 0
    maxCountry = ''
    for i in range(len(List)):
      if List[i].noOfWickets  > maxWicket:
        maxName = List[i].playerName 
        maxWicket = List [i].noOfWickets 
        maxCountry = List[i].playerCountry 
    print(maxName)
    print(maxWicket)
    print(maxCountry)
   
if __name__ == '__main__':
    count = int(input())
    List= []
    for i in range(count):
        playerName  = input()
        playerCountry = input()
        playerAge  = int(input())
        noOfMatches  = int(input())
        noOfRuns = int(input())
        noOfWickets  = int(input())                                                            
        List.append(Player(playerName,playerCountry,playerAge,noOfMatches,noOfRuns,noOfWickets))
Team1 = Team()
Team1.getMinRuns(List)
Team1.getMaxWickets(List)
    # cook your dish here
