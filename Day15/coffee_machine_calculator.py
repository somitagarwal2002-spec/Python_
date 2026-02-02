# Coffee Machine Calculator -------------------------------------------

menu = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
            "milk":0,
        },
        "cost":1.50
    },
    "latte":{
        "ingredients":{
            "water":200,
            "coffee":24,
            "milk":150,
        },
        "cost":2.50
    },
    "capuccino":{
        "ingredients":{
            "water":250,
            "coffee":24,
            "milk":100,
        },
        "cost":3.00
    },
}

resources = {
    "water":300,
    "coffee":100,
    "milk":200,
    "money":0.00
}

def espresso():
    if available_resources("espresso") is True:
        money_received = coins()
        changes(money_received, "espresso")
        print("Enjoy your espresso")
        new_resources("espresso")

def latte():
    if available_resources("latte") is True:
        money_received = coins()
        changes(money_received, "latte")
        print("Enjoy your latte")
        new_resources("latte")

def capuccino():
    if available_resources("cappucino") is True:
        money_received = coins()
        changes(money_received, "capuccino")
        print("Enjoy your cappucino")
        new_resources("cappucino")

def new_resources(coffee):
    resources["water"] -= menu[coffee]["ingredients"]["water"]
    resources["coffee"] -= menu[coffee]["ingredients"]["coffee"]
    resources["milk"] -= menu[coffee]["ingredients"]["milk"]

def available_resources(coffee):
    if resources["water"] < menu[coffee]["ingredients"]["water"]:
        print("Not enough water")
        return False
    
    elif resources["coffee"] < menu[coffee]["ingredients"]["coffee"]:
        print("Not enough coffee")
        return False
    
    elif resources["milk"] < menu[coffee]["ingredients"]["milk"]:
        print("Not enough coffee")
        return False
    
    else:
        return True

def changes(money_received, coffee):
    if (money_received < menu[coffee]["cost"]):
        print("Not enough money")

    elif (money_received == menu[coffee]["cost"]):
        print("Perfect")

    else:
        change = round(money_received - menu[coffee]["cost"], 2)
        print(f"Here's your change ${change}")
        resources["money"] += round((money_received - change), 2)

def coins():
    print("Please insert coins")
    try:
        quarter = int(input("How many quarters: "))
        dime = int(input("How many dime: "))
        nickel = int(input("How many nickel: "))
        penny = int(input("How many penny: "))
    except:
        print("Input int value only")
        quarter = int(input("How many quarters: "))
        dime = int(input("How many dime: "))
        nickel = int(input("How many nickel: "))
        penny = int(input("How many penny: "))

    return ( 0.25*quarter + 0.10*dime + 0.05*nickel + 0.01*penny )

condition = True
while condition:
    order = input("What would you like to have? (espresso/latte/capuccino): ").lower()

    if order == "report":
        print(f"Water: {resources['water']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Milk: {resources['milk']}")
        print(f"Money: {resources['money']}")

    elif order == "espresso":
        espresso()

    elif order == "latte":
        latte()

    elif order == "capuccino":
        capuccino()

    else:
        print("Chose correct option")

