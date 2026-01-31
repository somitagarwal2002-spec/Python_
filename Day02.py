print("Welcome to the tip calculator")
bill = float(input("What was the total bill? ₹"))
tip = float(input("How much tip would you like to give 10, 12, or 15? "))
no = int(input("How many people to split the bill? "))
per = (bill + (bill*12)/100)/5
print("Each person should pay:",per)
