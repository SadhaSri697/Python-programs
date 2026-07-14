def factorial(n):
    if(n==1 or n==1):
        return 1
    else:
        return n * factorial(n-1) # this is formula
    
n = int(input("Enter a Number: "))
print(f"The Factorial of this Number: {factorial(n)}")