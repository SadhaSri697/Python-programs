import random
n = random.randint(1,100) #randiant means it will chosse one num from 1 to 100
# random.randint is built in fuction
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess the number: "))
    if(a>n):
        print("Lower number please")
        guesses +=1
    elif(a<n):
        print("Higher number please")
        guesses +=1 

print(f"You have guessed the correct number {n} in {guesses} attempts")            