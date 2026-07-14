# to find sum of n natural numbers
def sum(n):
    if(n==1):
        return 1
    return n + sum(n-1)
        
n =  int(input("Enter a Number: "))
print(sum(n))