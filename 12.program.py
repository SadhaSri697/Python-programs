n = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")

#say hello only to names which starts from "s"or "S"
l = ["Sadha", "raji", "sisha","sravya","amrutha"]
for names in l:
    if names.upper().startswith("S"):     
        print(f"Hello {names}")    
        #see here programs for loop in code with harry 