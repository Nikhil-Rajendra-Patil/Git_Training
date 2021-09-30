class Movie:
    def init(self, id, name, cost, category="Default"):
        self.movie_id = id
        self.movie_name = name
        self.ticket_cost = cost
        self.category = category
    def assign_price_Category(self):
        if 0<self.ticket_cost<150:
            self.category = "General"
        elif 150<=self.ticket_cost<250:
            self.category = "Silver"
        elif 250<=self.ticket_cost<350:
            self.category = "Gold"
        else:
            self.category = "Platinum"
class Movie_Ticket:
    def init(self, customer_name, movie_name, viewerCount, totalTicketCost):
        self.customer_name = customer_name
        self.movie_name = movie_name
        self.viewerCount = viewerCount
        self.totalTicketCost = totalTicketCost
def getCategoryWiseCount(List):
    d = {}
    for x in List:
        if d.get(x.category) is None:
            d[x.category] = 1
        else:
            d[x.category] += 1
    return d
def bookMovieTicket(List,customer_name,movie_name,count_of_viewers):
    totalTicketCost = 0
    for x in List:
        if x.movie_name.lower()==movie_name.lower():
            totalTicketCost = x.ticket_cost*count_of_viewers
            ticket = Movie_Ticket(customer_name,movie_name,count_of_viewers,totalTicketCost)
            return ticket
    else:
        return None
List = []
n = int(input())
for _ in range(n):
    id = int(input())
    name = input()
    cost = int(input())
    movie = Movie(id,name,cost)
    movie.assign_price_Category()
    List.append(movie) 
custname = input()
moviename = input()
countofviewers = int(input())
d = getCategoryWiseCount(List)
print('Category wise ticket count')
for key in d.keys():
    print(str(key)+' : '+str(d[key]))
tik = bookMovieTicket(List,custname,moviename,countofviewers)
if tik==None:
    print("Movie not Available")
else:
    print(tik.customer_name,tik.totalTicketCost)