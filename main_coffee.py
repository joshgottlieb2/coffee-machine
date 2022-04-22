from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_status = "on"
money = 0
while machine_status == "on":
    choice = input(f"What would you like? ({menu.get_items()}): ")

    if choice == "report":
        coffee_maker.report()
    elif choice == "off":
        machine_status = "off"
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

