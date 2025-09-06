#Bill tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n$"))
tip = int(input("What percentage tip would you like to give? 10 12 15 \n"))
people=int(input("How many people to split the bill? \n"))
tip_amount=(tip/100)*bill
print((bill+tip_amount)/people)



