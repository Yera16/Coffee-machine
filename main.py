from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
options_available = menu.get_items()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while True:
    order = input (f"What do you want? {options_available}")
    if order == "report":
        coffee_maker.report()
        money_machine.report()
        continue
    elif order == "off":
        break
    else:
        drink = menu.find_drink(order)
        sufficient = coffee_maker.is_resource_sufficient(drink)

        if  sufficient == True:
            payment = money_machine.make_payment(drink.cost)
            if  payment == True:
                coffee_maker.make_coffee(drink)




