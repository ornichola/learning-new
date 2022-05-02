import random

numbers_of_friends = input('Enter the number of friends joining (including you): ')
print()

if not numbers_of_friends.isdigit() or int(numbers_of_friends) < 1:
    print('No one is joining for the party')
else:
    numbers_of_friends = int(numbers_of_friends)
    print('Enter the name of every friend (including you), each on a new line: ')
    bill = {input(): 0 for _ in range(numbers_of_friends)}
    print()
    total = int(input('Enter the total bill value: '))
    print()
    is_lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: \n') == 'Yes'
    if is_lucky:
        lucky = random.choice(list(bill.keys()))
        print(f'{lucky} is the lucky one!')
        numbers_of_friends -= 1
    else:
        print('No one is going to be lucky')
    print()
    bill = {k: round(total / numbers_of_friends, 2) for k in bill}
    if is_lucky:
        bill[lucky] = 0
    print(bill)
