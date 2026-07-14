# Function in class 
class student:
    name = "Sadha Sri"
    language = "Python"
    income = 50000

    def getintro(self): #here self is self parameter, it should be written to get output
        print(f"The is name is {self.name}. The language is {self.language}. The income is {self.income}")
        # in place of self we use anything.
    def greet(self):
        print("Good Morning") #see in this there is no need of obj , so we don't need 
                              #self parameter
    @staticmethod #this static method where we use when we don't obj
    def greet():
        print("Good Morning")                         

sadha = student() #here sadha is object
sadha.greet()
sadha.greet()
sadha.getintro()

