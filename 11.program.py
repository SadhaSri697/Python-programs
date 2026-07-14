numbers = []
for num in range(4):
    num = int(input(f"Enter Number {num+1} : "))
    numbers.append(num)
    
greatest = numbers[0]

for num in numbers:
    if num > greatest:
        greatest = num

print("The Greatest Number = ",greatest) 