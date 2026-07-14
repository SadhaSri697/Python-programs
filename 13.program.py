def number():
    a = int(input("Enter a Number: " ))
    b = int(input("Enter a Number: " ))
    c = int(input("Enter a Number: " ))
    if(a>b and a>c):
        print("the greatest number: ",a)
    elif(b>a and b>c):
        print("the greatest number: ",b)
    else:
        print("the greatest number: ",c)   

number()        
            