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

water=300
milk =200
cof = 100
money = 0
print(MENU)
def coffeemachine():
    global water 
    global milk
    global cof
    global money
    inp1='y'
    while inp1=='y':
        coffee=input("What would you like? (espresso/latte/cappuccino) - ")
        coffee=coffee.lower()
        if coffee=='espresso' or coffee=='latte' or coffee=='cappuccino':
            inp1='n'
        elif coffee=="report":
            print("Water: ", water, "ml")
            print("Milk: ", milk, "ml")
            print("Coffee: ", cof, "g")
            print("Money: $", money)
            inp1='n'
            coffeemachine()
        else:
            print("Invalid Input")
            inp1=(input("Do you wish to continue: (Y - Yes| N - No): "))
            inp1=inp1.lower()
    print("Please Insert Coins.")
    qua=int(input("How many quarters? - "))
    dim=int(input("How many dimes? - "))
    nic=int(input("How many nickles? - "))
    pen=int(input("How many pennies? - "))
    total = (qua*0.25) + (dim*0.10) + (nic*0.05) + (pen*0.01)
    if coffee=='espresso':
        cost = MENU["espresso"]["cost"]
        if cost>total:
            print("Sorry that's not enough money, Money refunded.")
            coffeemachine()
        else:
            if water > MENU["espresso"]["ingredients"]["water"]:
                water=water-MENU["espresso"]["ingredients"]["water"]
            else:
                print("Sorry there is not enough water.")
                coffeemachine()
            if cof > MENU["espresso"]["ingredients"]["coffee"]:
                cof=cof-MENU["espresso"]["ingredients"]["coffee"]
            else:
                print("Sorry there is not enough coffee.")
                coffeemachine()
    elif coffee=='latte':
        cost = MENU["latte"]["cost"]
        if cost>total:
            print("Sorry that's not enough money, Money refunded.")
            coffeemachine()
        else:
            if water > MENU["latte"]["ingredients"]["water"]:
                water=water-MENU["latte"]["ingredients"]["water"]
            else:
                print("Sorry there is not enough water.")
                coffeemachine()
            if cof > MENU["latte"]["ingredients"]["coffee"]:
                cof=cof-MENU["latte"]["ingredients"]["coffee"]
            else:
                print("Sorry there is not enough coffee.")
                coffeemachine()
            if milk > MENU["latte"]["ingredients"]["milk"]:
                milk=milk-MENU["latte"]["ingredients"]["milk"]
            else:
                print("Sorry there is not enough milk.")
                coffeemachine()
    elif coffee=='cappuccino':
        cost = MENU["cappuccino"]["cost"]
        if cost>total:
            print("Sorry that's not enough money, Money refunded.")
            coffeemachine()
        else:
            if water > MENU["cappuccino"]["ingredients"]["water"]:
                water=water-MENU["cappuccino"]["ingredients"]["water"]
            else:
                print("Sorry there is not enough water.")
                coffeemachine()
            if cof > MENU["cappuccino"]["ingredients"]["coffee"]:
                cof=cof-MENU["cappuccino"]["ingredients"]["coffee"]
            else:
                print("Sorry there is not enough coffee.")
                coffeemachine()
            if milk > MENU["cappuccino"]["ingredients"]["milk"]:
                milk=milk-MENU["cappuccino"]["ingredients"]["milk"]
            else:
                print("Sorry there is not enough milk.")
                coffeemachine()
    change=round(total-cost,2)
    print("Here is your change: $",change )
    print("Here is your", coffee, "Enjoy!")
    coffeemachine()
coffeemachine()
