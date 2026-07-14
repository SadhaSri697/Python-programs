#PROJECT 
#🐍Snake,💦Water,🔫Gun
'''
1 = snake
-1 = water 
0 = gun
'''
import random # this is function which helps computer to choice a option in given
computer = random.choice([1,-1,0])
youstr = input("Enter your choice: ")
youDict = {"snake":1 ,"water":-1, "gun":0}
reverseDict = {1:"snake", -1:"water",0:"gun"}

you = youDict[youstr]

print(f"your chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(you == computer):
    print("its a Draw")
else:
    if(computer ==-1 and you==1): 
        print("You Win!")
    elif(computer ==1 and you==-1): 
        print("You Lose!")
    elif(computer ==0 and you==-1):  
        print("You Lose!")
    elif(computer ==-1 and you==0): 
        print("You Win!")
    elif(computer ==1 and you==0):
        print("You Win!")
    elif(computer ==0 and you==1):
        print("You Lose!")
    else:
        print("Something went Wrong")    

# shorted program
# if(you-computer == -1 or you-computer == 2):
#    print("You Lose!")
# else:
#    print("You Win!")         
