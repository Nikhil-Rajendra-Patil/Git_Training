class Sponsors:
    def __init__(self,sponsorName,sponsorCompany,subsidiaries,sponsorCategory):
        self.sponsorName = sponsorName
        self.sponsorCompany = sponsorCompany
        self.subsidiaries = subsidiaries
        self.sponsorCategory = sponsorCategory

def getSponsor(self,sponsorList,sponsorCategoryrequired):
    l =[]
    for i in sponsorList:333333
        if i.sposorCategory.lower() == sponsorCategoryrequired.lower():
            l.append(i)
    l.sort(key=lambda i: i.sposorName)
    if len(l) > 0:
        return l
    else:
        return None

def findSponsorWithMaximumSubsidiaries(sponsorList):
    sponsorList.sort(key = lambda i: len(i.subsidiaries),reverse=True)
    if len(sponsorList) > 0:
        return sponsorList[0].sponsorName
    else :
        return None

if __name__ == '__main__':
    count = int(input())
    sponsorList = []
    for i in range(count):
        sponsorName = input()
        sponsorCompany = input()
        subsidiaries = []
        sub_count = int(input())
        for i in range(sub_count):
            subsidiary = input()
            subsidiaries.append(subsidiary)
        sponsorCategory = input()
        Sponsor = Sponsors(sponsorName, sponsorCompany, subsidiaries, sponsorCategory)
        sponsorList.append(Sponsor)

    sponsorCategoryrequired = input()

    SponsorWithMaximumSubsidiaries = findSponsorWithMaximumSubsidiaries(sponsorList)

    getSponsorList = getSponsor(sponsorList,sponsorCategoryrequired)
    if getSponsorList is None:
        print('No matching record found.')
    else:
        for i in getSponsorList:
            print(i.sponsorName)
    
    print(SponsorWithMaximumSubsidiaries)


print()