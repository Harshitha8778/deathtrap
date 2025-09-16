#SILENT AUCTION
from art import logo
print(logo)
cont = "Y"
bidders = {}
while cont == "Y":
    print("\n"*50)
    name = input("What is your name? ")
    bids = int(input("How much would you like to bid? $"))
    bidders[name] = bids
    cont = input("Anyone else wants to bid, Y or N: ")
if cont == "N":
    for name in bidders:
        max = 0
        winner = ""
        if bidders[name] > max:
            max = bidders[name]
        winner = name
    print("SOLD! the item goes to",name)




