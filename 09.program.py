#check if given username is having less than 10 Character or not
username = input("Enter Unsername: ")

if(len(username)==10):
    print("Username Saved!")
elif(len(username)>10):
    print("Enter below 10 Character  Or 10 Character")        
else:
    print("Enter below 10 Character Or 10 Character")    