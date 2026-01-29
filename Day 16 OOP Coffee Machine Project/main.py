from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

power = True

while power == True:
    choice = input(f"\nWhat would you like? {menu.get_items()}: ")
    #menuitem = None
    if choice == "off":
        power = False
    elif choice == "report":
        coffeemaker.report()
        moneymachine.report()
    else:
        menuitem = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(menuitem):
            if moneymachine.make_payment(menuitem.cost):
                coffeemaker.make_coffee(menuitem)