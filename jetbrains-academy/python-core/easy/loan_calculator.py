import argparse
import math
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--type', choices=['annuity', 'diff'])
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')

args = parser.parse_args()

required_args = args.type or args.interest
args_length = len({k: v for k, v in vars(args).items() if v})
incorrect_following_args = args.type == 'diff' and args.payment
negative_args = any(str(arg).startswith('-') for arg in vars(args).values() if arg)
if not required_args or args_length < 4 or incorrect_following_args or negative_args:
    print('Incorrect parameters')
    exit()

payment_type = args.type

if payment_type == 'diff':
    interest = float(args.interest)
    principal = float(args.principal)
    periods = int(args.periods)
    monthly_interest_rate = interest / (12 * 100)
    total = 0
    for i, _ in enumerate(range(periods), start=1):
        mp = math.ceil(principal / periods + monthly_interest_rate * (principal - principal * (i - 1) / periods))
        total += mp
        print(f'Month {i}: payment is {mp}')

    print(f'\nOverpayment = {total - principal}')

if payment_type == 'annuity':

    if not args.payment:  # wrong
        interest = float(args.interest)
        principal = float(args.principal)
        periods = int(args.periods)

        nominal_interest_rate = interest / (12 * 100)
        monthly_payment = principal * (nominal_interest_rate * math.pow(1 + nominal_interest_rate, periods)) / (math.pow(1 + nominal_interest_rate, periods) - 1)
        print(f'Your monthly payment = {math.ceil(monthly_payment)}!')
        print(f'Overpayment = {periods * math.ceil(monthly_payment) - principal}')

    if not args.periods:
        interest = float(args.interest)
        principal = float(args.principal)
        payment = int(args.payment)

        nominal_interest_rate = interest / (12 * 100)
        number_of_months = math.ceil(math.log(payment / (payment - nominal_interest_rate * principal), 1 + nominal_interest_rate))
        years = math.floor(number_of_months / 12)
        months = number_of_months - years * 12
        years_str = 'years' if years > 1 else 'year'
        months_str = 'months' if months > 1 else 'month'
        if years and months:
            print(f'It will take {years} {years_str} and {months} {months_str} to repay this loan!')
        if years and not months:
            print(f'It will take {years} {years_str} to repay this loan!')
        if not years and months:
            print(f'It will take {months} {months_str} to repay this loan!')
        print(f'Overpayment = {number_of_months * payment - principal}')

    if not args.principal:
        interest = float(args.interest)
        periods = float(args.periods)
        payment = int(args.payment)

        nominal_interest_rate = interest / (12 * 100)
        principal = payment / (nominal_interest_rate * (math.pow(1 + nominal_interest_rate, periods)) / (math.pow(1 + nominal_interest_rate, periods) - 1))
        print(f'Your loan principal = {math.floor(principal)}!')
        print(f'Overpayment = {math.ceil(periods * payment - principal)}')
