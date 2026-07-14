class student:
    language = "Python"
    income = 50000

    def __init__(self,name,language,income): # Dunder method which is automatically called
        self.name = name
        self.language = language 
        self.income = income
        print("i am creating an object")
    
sadha = student("Sadha Sri","java",60000)
print(sadha.name , sadha.language , sadha.income)
#see here we no need to create obj for init
#__init__(self) is constructor
