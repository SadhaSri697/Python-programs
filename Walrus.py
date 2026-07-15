#using warlus operator
if (n := len([1,2,3,4,5])) > 3:
    print(f"List is too long ({n} elements , expected <= 3)")
else:
    print("List is perfect with 3 numbers")   
# here n := len([1,2,3,4,5]) is written in one that's use of walrus    
