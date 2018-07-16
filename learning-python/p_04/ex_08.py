def is_prime(number):
    x = number // 2
    while x > 1:
        if number % x == 0:
            print(number, 'has factor', x)
            break
        x = x - 1
    else:
        print(number, 'is prime')


is_prime(1)
is_prime(2)
is_prime(3)
is_prime(4)
is_prime(5)
is_prime(6)
is_prime(7)
is_prime(8)
is_prime(9)
is_prime(13)
is_prime(13.0)
is_prime(15)
is_prime(15.0)
