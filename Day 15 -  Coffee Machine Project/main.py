from menu import MENU,resources,coins

power = True


# Function that returns 'g' for coffee, 'ml' otherwise
def ml_or_g(ingredient):
    if ingredient == "coffee":
        return "g"
    else:
        return "ml"

# Function that shows current resource levels when 'report' is typed and entered.
def report():
    print("Current Resources")
    for item in resources:
        print(f"{item}: {resources[item]}{ml_or_g(item)}")

#Function that checks if there are enough resources to make the chosen drink
#Returns True if there is or prints the resource(s) that are lacking if not
def check_resources(drink):
    can_make = True
    reasons_not = []
    for ingredient in MENU[drink]["ingredients"]:
        if ingredient in resources:
            if MENU[drink]['ingredients'][ingredient] > resources[ingredient]:
                reasons_not.append(f"not enough {ingredient}: {MENU[drink]['ingredients'][ingredient]}{ml_or_g(ingredient)} "
                                   f"required, {resources[ingredient]}{ml_or_g(ingredient)} available")
                can_make = False

    if can_make:
        return True
    else:
        for reason in reasons_not:
            print(reason)

#Function to deduct resources once a drink has been made
def deduct_resource():
    for resource in resources:
        if resource in MENU[choice]["ingredients"]:
            resources[resource] -= MENU[choice]["ingredients"][resource]

#Function that returns the total value of the coins that are entered
def process_coins():
    total = 0
    print(f"Price of {choice} = ${MENU[choice]['cost']}")
    print("Please insert coins")
    for coin in reversed(coins):
        total += float(input(f"how many {coin}s?:")) * coins[coin]

    return total

#Function the returns change and makes drink if more than enough money is entered, Makes the drink if correct
#money entered or gives sorry message if not enough entered. Also deducts resources if drink is made.
def transaction_successful(cash):
    serve = (f"Here is your {choice} ☕️. Enjoy!")
    if cash > MENU[choice]["cost"]:
        print(f"Here is your ${cash - MENU[choice]['cost']:.2f} change")
        print(serve)
        print("\n" * 3)
        deduct_resource()
    elif cash == MENU[choice]['cost']:
        print(serve)
        print("\n" * 3)
        deduct_resource()
    else:
        print("Sorry that's not enough money. Money refunded.")
        print("\n" * 3)

#While loop to keep the program running until 'off' is typed
#Also added a function to refill the resources.
while power == True:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ")

    #Function to end the program if 'off' is typed and entered.
    def power_down():
        global power
        print("Powering down")
        power = False

    if choice == "off":
        power_down()
    elif choice == "report":
        report()
    elif choice == "refill":
        for resource in resources:
            resources[resource] = 300
    else:
        if check_resources(choice):
            transaction_successful(process_coins())


