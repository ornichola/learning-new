class CoffeeMachine:
    def __init__(self, money: int = 550, water: int = 400, milk: int = 540, beans: int = 120, cups: int = 9):
        self.money = money
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.coffee_types = (
            {
                'name': 'espresso',
                'water': 250,
                'milk': 0,
                'beans': 16,
                'price': 4,
            },
            {
                'name': 'latte',
                'water': 350,
                'milk': 75,
                'beans': 20,
                'price': 7,
            },
            {
                'name': 'cappuccino',
                'water': 200,
                'milk': 100,
                'beans': 12,
                'price': 6,
            }
        )

    def __str__(self):
        resources = [
            f'{self.water} of water',
            f'{self.milk} of milk',
            f'{self.beans} of coffee beans',
            f'{self.cups} of disposable cups',
            f'${self.money} of money',
        ]
        return 'The coffee machine has:\n' + '\n'.join(resources)

    def _check_resources(self, coffee_type):
        state = {
            'is_enough': None,
            'reason': '',
        }
        ct = self.coffee_types[coffee_type]
        if self.water < ct['water']:
            state['is_enough'], state['reason'] = False, 'water'
        elif self.milk < ct['milk']:
            state['is_enough'], state['reason'] = False, 'milk'
        elif self.beans < ct['beans']:
            state['is_enough'], state['reason'] = False, 'coffee beans'
        elif self.cups < 0:
            state['is_enough'], state['reason'] = False, 'cups'
        else:
            state['is_enough'] = True
        return state

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def fill(self, water: int, milk: int, beans: int, cups: int):
        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups

    def buy(self, choice: str):
        if choice == 'back':
            return
        index = int(choice) - 1
        state = self._check_resources(index)
        if not state['is_enough']:
            print(f'Sorry, not enough {state["reason"]}!')
        else:
            print('I have enough resources, making you a coffee!')
            self.cups -= 1
            self.water -= self.coffee_types[index]['water']
            self.milk -= self.coffee_types[index]['milk']
            self.beans -= self.coffee_types[index]['beans']
            self.money += self.coffee_types[index]['price']

    def work_on(self):
        while True:
            action = input('Write action (buy, fill, take, remaining, exit): ')
            if action == 'exit':
                return
            elif action == 'buy':
                self.buy(
                    input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
                )
            elif action == 'fill':
                self.fill(
                    water=int(input('Write how many ml of water you want to add: ')),
                    milk=int(input('Write how many ml of milk you want to add: ')),
                    beans=int(input('Write how many grams of coffee beans you want to add: ')),
                    cups=int(input('Write how many disposable cups of coffee you want to add: ')),
                )
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                print(self)
            else:
                continue


CoffeeMachine().work_on()
