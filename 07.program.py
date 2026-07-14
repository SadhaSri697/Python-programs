#enter 4 four num and say greatest in it 
a1 = int(input("Enter Number 1: "))
a2 = int(input("Enter Number 2: "))
a3 = int(input("Enter Number 3: "))
a4 = int(input("Enter Number 4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Number 1 is Greatest : " ,a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("Number 2 is Greatest : " ,a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("Number 3 is Greatest : " ,a3)
else:
    print("Number 4 is Greatest : ",a4)
              
    