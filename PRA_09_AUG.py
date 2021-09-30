class City:
    def __init__ (self,cityId,stateName,cityName,rainfallReceived,year):
        self.cityId = cityId
        self.stateName = stateName
        self.cityName = cityName
        self.rainfallReceived = rainfallReceived
        self.year = year

class RainfallAnalysis:
    def __init__ (self,cityList):
        self.cityList = cityList

    def getStateWiseRainfall(cityList):
        citySort = cityList.sort(key = lambda e: e['i.stateName'])

        for i in citySort:
            print(i.cityName, i.rainfallReceived)


    def findCitiesWithMoreThanAvgRainfall(state,cityList):
        Rainfall = 0
        AvgRainFall = 0
        count  = 0
        City = {}
        for i in cityList:
            if i.stateName.lower() == state.lower():
                Rainfall = i.rainfallReceived + Rainfall
                count = count + 1

        AvgRainFall = Rainfall/count

        for i in cityList:
            if i.rainfallReceived >= AvgRainFall:
                City{i.cityName} = i.rainfallReceived
            
        return City

if __name__ =="__main__":
    n = int(input())
    cityList = []
    for i in range(n):
        cityId = int(input())
        stateName = input()
        cityName = input()
        rainfallReceived = int(input())
        year = int(input())
        cityList.append(cityId,stateName,cityName,rainfallReceived,year)

    state = input()