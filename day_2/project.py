print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? (10, 12, or 15) "))
people = int(input("How many people to split the bill? "))

pp_pay = round((bill / people) * ((tip/100)+1),2)

print(f"Each person should pay: ${pp_pay}")
