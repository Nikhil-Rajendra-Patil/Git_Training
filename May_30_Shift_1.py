class Citizen:
    def __init__(self,citizenID,citizenName,citizenAge,isFrontLineWorker,vaccineOptedFor):
        self.citizenID = citizenID;
        self.citizenName = citizenName;
        self.citizenAge = citizenAge;
        self.isFrontLineWorker = isFrontLineWorker;
        self.vaccineOptedFor = vaccineOptedFor;
        #self.preference = preference;

    def setPreference(self):
        if self.isFrontLineWorker.lower() == "yes" or self.citizenAge > 45:
            self.preference = 1;
        else :
            self.preference = 0;

class VaccinationDrive:
    def __init__(self,cList):
        self.cList = cList
        pass
    def PreferredVaccinationCount(self):
        count = 0
        for i in self.cList:
            if i.preference == 1:
                count += 1;
        if count == 0:
            return None;
        else:
            return count;
    
    def getCitizenAsPerVaccine(self,V_name):
        count1 = 0
        l = []
        for i in self.cList:
            if i.vaccineOptedFor.lower() == V_name.lower() :
                count1 += 1
                l.append(i)
        l.sort(key=lambda k: k.citizenAge)
        if count1 == 0:
            return None
        else:
            return l

if __name__ == '__main__':
    count = int(input())
    cList = []
    for i in range(count):
        citizenID = input()
        citizenName = input()
        citizenAge = int(input())
        isFrontLineWorker = input()
        vaccineOptedFor = input()
        Citizen = Citizen(citizenID,citizenName,citizenAge,isFrontLineWorker,vaccineOptedFor)
        Citizen.setPreference()
        cList.append(Citizen)

VaccinationDrive = VaccinationDrive(cList)
V_Name = input()
PreferedVaccinationCount = VaccinationDrive.PreferredVaccinationCount()
CitizenAsPerVaccine = VaccinationDrive.getCitizenAsPerVaccine()

if CitizenAsPerVaccine is None:
    print("Citizen not found")
else:
    for i in cList:
        print(i.citizenID)
        print(i.citizenName)
        print(i.citizenAge)
    
if PreferedVaccinationCount is None:
    print("Preferred Citizen not found")
else:
    print(PreferedVaccinationCount)



