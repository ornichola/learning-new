import requests


HOST = 'http://www.floatrates.com/daily'
CACHED_RATES = dict()


def add_cache(code: str = ''):
    rates = requests.get(f'{HOST}/{my_currency_code}.json').json()
    if not code:
        CACHED_RATES['usd'] = rates.get('usd')
        CACHED_RATES['eur'] = rates.get('eur')
    else:
        CACHED_RATES[code] = rates.get(code)


def get_rate(code: str):
    code = code.lower()
    print('Checking the cache...')
    if not CACHED_RATES.get(code):
        print('Sorry, but it is not in the cache!')
        add_cache(code)
    else:
        print('Oh! It is in the cache!')

    return CACHED_RATES.get(code)['rate']


my_currency_code = input()
add_cache()
while True:
    exchange_currency_code = input()
    if not exchange_currency_code:
        break
    exchanged = round(float(input()) * get_rate(exchange_currency_code), 2)
    print(f'You received {exchanged} {exchange_currency_code}.')
