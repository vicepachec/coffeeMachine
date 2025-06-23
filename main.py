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

money = 0
machine_on = True

def check_resources(water, milk, coffee):
	if water > resources["water"]:
		print("Sorry there is not enough water")
	elif milk > resources["milk"]:
		print("Sorry there is not enough milk")
	elif coffee > resources["coffee"]:
		print("Sorry there is not enough coffee")
	else:
		return True
	
def money_handle():
	total = 0
	total += 0.25 * float(input("how many quarters: "))
	total += 0.10 * float(input("how many dimes: "))
	total += 0.05 * float(input("how many nickels: "))
	total += 0.01 * float(input("how many pennies: "))
	total = round(total, 2)
	return total

def make_drink(drink, ingredients):
	for item in ingredients:
		resources[item] -= ingredients[item]
	print(f"Here is your {drink}. Enjoy!")

while machine_on:
	choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
	if choice == "off":
		machine_on = False
	elif choice == "report":
		print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g\n"
		f"Money: ${money}")
	elif choice in MENU:
		drink = MENU[choice]
		ingredients = drink["ingredients"]
		cost = drink["cost"]
		if check_resources(ingredients["water"], 0, ingredients["coffee"]):
			print("Please insert coins")
			inserted = money_handle()
			if inserted < cost:
				print("Sorry that's not enough money. Money refunded.")
			else:
				change = inserted - cost
				if change > 0:	
					print(f"The change is {inserted - cost}.")
				money += cost
				make_drink(choice, ingredients)
		else:
			print("Please call a technician.")
	else:
		print("That's not a valid input")