name = input("Enter your name : ")
print("Good afernoon", name)

letter = ''' Dear Name
        YOUR ARE SELECTED!
        Date'''
print(letter.replace("Name",name).replace("Date","6th Sep 2029"))