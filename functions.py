#Function Definition
def avg():
    a = int(input("Enter Number: "))
    b = int(input("Enter Number: "))
    c = int(input("Enter Number: "))
    average = (a+b+c)/3
    print(average) 
#Function Call
for num in range(5):    # here i used for loop to call fun 
    avg()    
    print("Thank You") 
# there is another way we need to type 5 times to call func 5 times like
#avg()
#avg()
#avg()
#avg()
#avg()
