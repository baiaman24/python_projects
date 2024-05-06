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
PROFIT = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    """Prints out the existing resources"""
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${PROFIT}")


def complete_order(coffee, paid_amount):
    """Completes the order made, renews resources and accumulates profit """
    global PROFIT
    ordered_coffee = MENU[coffee]
    water_amount_needed = ordered_coffee["ingredients"]["water"]
    coffee_amount_needed = ordered_coffee["ingredients"]["coffee"]
    cost_of_coffee = ordered_coffee["cost"]
    resources["water"] -= water_amount_needed
    resources["coffee"] -= coffee_amount_needed
    PROFIT += cost_of_coffee
    if coffee != "espresso":
        milk_amount_needed = ordered_coffee["ingredients"]["milk"]
        resources["milk"]-=milk_amount_needed
    change = round(paid_amount - cost_of_coffee)
    if change != 0:
        print(f"Here is ${change} in change")
    print(f"Here is your {coffee} ☕. Enjoy!")


def is_money_enough(order, paid_amount):
    """Checks whether money is enough for the chosen drink"""
    cost = MENU[order]["cost"]
    if cost <= paid_amount:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def are_resources_enough(ordered_coffee):
    """Checks whether resources are enough to make a chosen drink"""
    ingredients = MENU[ordered_coffee]["ingredients"]
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


should_work = True
while should_work:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice != "report" and choice != "off":
        if are_resources_enough(choice):
            print("Please insert coins.")
            quarter = int(input("how many quarters?: "))
            dime = int(input("how many dimes?: "))
            nickel = int(input("how many nickels?: "))
            penny = int(input("how many pennies?: "))
            total_accepted = quarter * 0.25 + dime * 0.1 + nickel * 0.05 + penny * 0.01
            if is_money_enough(choice, total_accepted):
                complete_order(choice, total_accepted)
    elif choice == "report":
        report()
    elif choice == "off":
        should_work = False

