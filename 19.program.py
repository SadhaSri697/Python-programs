#list of microsoft emoploy
class programmer:
    company = "Microsoft"
    def __init__(self,name,income,pin):
        self.name = name
        self.income = income
        self.pin = pin

p = programmer("Sadha",600000,69777)
print(p.name,p.income,f"pin-{p.pin}",p.company)   
r = programmer("Rohan",500000,60987)
print(r.name,r.income,f"pin-{r.pin}",r.company)    
