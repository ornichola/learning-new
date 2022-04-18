coffee = {
    '1': {
        'name': 'espresso',
        'water': 250,
        'milk': 0,
        'beans': 16,
        'price': 4,
    },
    '2': {
        'name': 'latte',
        'water': 350,
        'milk': 75,
        'beans': 20,
        'price': 7,
    },
    '3': {
        'name': 'cappuccino',
        'water': 200,
        'milk': 100,
        'beans': 12,
        'price': 6,
    },
}

coffee_machine = {
    'money': 550,
    'water': 400,
    'milk': 540,
    'beans': 120,
    'cups': 9,
}


def show_state():
    print('The coffee machine has:')
    print(f"{coffee_machine['water']} ml of water")
    print(f"{coffee_machine['milk']} ml of milk")
    print(f"{coffee_machine['beans']} g of coffee beans")
    print(f"{coffee_machine['cups']} disposable cups")
    print(f"${coffee_machine['money']} of money")


def _check_resources(coffee_type):
    state = {
        'is_enough': None,
        'reason': '',
    }
    ct = coffee[coffee_type]
    if coffee_machine['water'] < ct['water']:
        state['is_enough'], state['reason'] = False, 'water'
    elif coffee_machine['milk'] < ct['milk']:
        state['is_enough'], state['reason'] = False, 'milk'
    elif coffee_machine['beans'] < ct['beans']:
        state['is_enough'], state['reason'] = False, 'coffee beans'
    elif coffee_machine['cups'] < 0:
        state['is_enough'], state['reason'] = False, 'cups'
    else:
        state['is_enough'] = True
    return state


def buy():
    global coffee_machine
    choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
    if choice == 'back':
        return
    state = _check_resources(choice)
    if not state['is_enough']:
        print(f'Sorry, not enough {state["reason"]}!')
    else:
        print('I have enough resources, making you a coffee!')
        coffee_machine['cups'] -= 1
        coffee_machine['water'] -= coffee[choice]['water']
        coffee_machine['milk'] -= coffee[choice]['milk']
        coffee_machine['beans'] -= coffee[choice]['beans']
        coffee_machine['money'] += coffee[choice]['price']


def fill():
    global coffee_machine
    coffee_machine['water'] += int(input('Write how many ml of water you want to add: '))
    coffee_machine['milk'] += int(input('Write how many ml of milk you want to add: '))
    coffee_machine['beans'] += int(input('Write how many grams of coffee beans you want to add: '))
    coffee_machine['cups'] += int(input('Write how many disposable cups of coffee you want to add: '))


def take():
    global coffee_machine
    print(f'I gave you ${coffee_machine["money"]}')
    coffee_machine['money'] = 0


actions = {
    'buy': buy,
    'fill': fill,
    'take': take,
    'remaining': show_state,
}


while True:
    action = input('Write action (buy, fill, take, remaining, exit): ')
    if action == 'exit':
        break
    actions[action]()
