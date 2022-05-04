LOGO = '''
 ██████  ██████  ███████ ███████ ███████ ███████     ███    ███  █████   ██████ ██   ██ ██ ███    ██ ███████ 
██      ██    ██ ██      ██      ██      ██          ████  ████ ██   ██ ██      ██   ██ ██ ████   ██ ██      
██      ██    ██ █████   █████   █████   █████       ██ ████ ██ ███████ ██      ███████ ██ ██ ██  ██ █████   
██      ██    ██ ██      ██      ██      ██          ██  ██  ██ ██   ██ ██      ██   ██ ██ ██  ██ ██ ██      
 ██████  ██████  ██      ██      ███████ ███████     ██      ██ ██   ██  ██████ ██   ██ ██ ██   ████ ███████ 
                                                                                                                                                                                                                        
'''
print(LOGO)
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
water_resource = resources["water"]
milk_resource = resources["milk"]
coffee_resource = resources["coffee"]
resources["money"] = 0
sufficient_resources = True
while sufficient_resources:
    print("Espresso: $1.50\nLatte: $2.50\nCappuccino: $3.00")
    drink = input("What would you like? (espresso, latte, cappuccino): ")
    if drink == "off":
        break
    if drink == "report":
        for resource in resources:
            print(f"{resource}: {resources[resource]}")
    else:
        if drink == "espresso":
            water_resource = resources["water"] - MENU["espresso"]["ingredients"]["water"]
            coffee_resource = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        if drink == "latte":
            water_resource = resources["water"] - MENU["latte"]["ingredients"]["water"]
            milk_resource = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
            coffee_resource = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        if drink == "cappuccino":
            water_resource = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            milk_resource = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
            coffee_resource = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]

        if water_resource < 0:
            print("Sorry, but there is not enough water in the machine")
        if milk_resource < 0:
            print("Sorry, but there is not enough milk in the machine")
        if coffee_resource < 0:
            print("Sorry, but there is not enough coffee in the machine")

        if water_resource > 0 and milk_resource > 0 and coffee_resource > 0:
            resources["water"] = water_resource
            resources["milk"] = milk_resource
            resources["coffee"] = coffee_resource
            print("Please insert coins")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
            print(f"Total paid: ${total}")
            change = round(total - MENU[drink]["cost"], 2)
            if change < 0:
                print("Not enough money")
            else:
                print(f"Here is your ${change} in change")
                resources["money"] += MENU[drink]["cost"]
                print(f"Here is your {drink}! Enjoy!")
        if resources["water"] < 50 or resources["coffee"] < 18:
            print("Insufficient resources for any order")
            sufficient_resources = False
print("Coffee Machine is off. Goodbye")
