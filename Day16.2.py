import sys
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu,MenuItem
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while True:
    print(menu.get_items())
    order_name = input("What do you want to drink?: ")
    if order_name == "report":
        coffee_maker.report()
    elif order_name == "cash":
        money_machine.report()
    elif order_name in menu.get_items():
        if menu.find_drink(order_name):
            item = menu.find_drink(order_name)
            if (coffee_maker.is_resource_sufficient(item)):
                cost = item.cost
                payment = money_machine.make_payment(cost)
                if payment:
                    order = item
                    coffee_maker.make_coffee(order)
    elif order_name == "off":
        sys.exit()
    






    
