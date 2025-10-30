import sys
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def sufficient(choice):
    if resources['water'] >= MENU[choice]['ingredients']['water'] :
        if resources['coffee'] >= MENU[choice]['ingredients']['coffee']:
            if 'milk' in MENU[choice]['ingredients']:
                if resources['milk'] >= MENU[choice]['ingredients']['milk']:
                    return True
                else:
                    return print("sorry, there's not enough milk")
            else:
                return True
        else:
            return print("sorry, there's not enough coffee")
    else:
        return print("sorry, there's not enough water")

def coins():
    print("please insert coins:")
    quarters = int(input("how many quarters? "))
    dimes = int(input("how many dimes? "))
    nickels = int(input("how many nickels? "))
    pennies = int(input("how many pennies? "))
    sum: float = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return sum

def paid(payment,choice):
    if payment < MENU[choice]["cost"]:
        return print("Not enough, your money is refunded")
    elif payment == MENU[choice]['cost']:
        return True
    elif payment > MENU[choice]['cost']:
        change = payment - MENU[choice]['cost']
        print("Here's your change $",change)
        return True

def coffee(choice,resources):
    resources['water'] -= MENU[choice]['ingredients']['water']
    resources['coffee'] -= MENU[choice]['ingredients']['coffee']
    if 'milk' in MENU[choice]['ingredients']:
        resources['milk'] -= MENU[choice]['ingredients']['milk']
    print("your ",choice,"is ready, enjoy".title())

def report():
    return print(resources)

def refill():
    item = input("What would you like to refill? ")
    quantity = int(input("How much would you like to add? "))
    resources[item] += quantity

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'report':
        report()
    elif choice == 'off':
        sys.exit()
    else:
        if sufficient(choice):
            payment = coins()
            if paid(payment,choice):
                coffee(choice, resources)
        else:
            print("Please Refill")
            refill()





