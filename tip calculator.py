#print welcome
print("Welcome to the tip calculator!")
#ask what the total bill is
total = float(input("What was the total bill? $"))
#ask how much tip they want to give
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
#ask how many people are splitting the bill
num_people = int(input("How many people to split the bill? "))
#make a calculation for what each person should pay
calc = round(total * (1 + tip/100) / num_people , 2)
#output how much each person should pay
print(f"Each person should pay: {calc}")