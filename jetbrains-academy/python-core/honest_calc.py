MESSAGES = [
    "Enter an equation",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):",
    "Do you want to continue calculations? (y / n):",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    "You are",
    "Are you sure? It is only one digit! (y / n)",
    "Don't be silly! It's just one number! Add to the memory? (y / n)",
    "Last chance! Do you really want to embarrass yourself? (y / n)",
]
msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12 = MESSAGES


def is_one_digit(var):
    return var.is_integer() and -10 < var < 10


def check(var1, var2, var3):
    msg = ''
    if is_one_digit(var1) and is_one_digit(var2):
        msg = msg + msg_6
    if (var1 == 1 or var2 == 1) and var3 == '*':
        msg = msg + msg_7
    if (var1 == 0 or var2 == 0) and (var3 in ('+', '-', '*')):
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)
    else:
        return


memory = 0.0
while True:
    print(msg_0)
    x, operation, y = input().split()

    try:
        if x == 'M':
            x = memory
        else:
            x = float(x)
        if y == 'M':
            y = memory
        else:
            y = float(y)
    except ValueError:
        print(msg_1)
        continue

    if operation not in ('+', '-', '*', '/'):
        print(msg_2)
        continue
    else:
        result = 0.0
        check(x, y, operation)
        if operation == '+':
            result = x + y
        if operation == '-':
            result = x - y
        if operation == '*':
            result = x * y
        if operation == '/':
            if y != 0:
                result = x / y
            else:
                print(msg_3)
                continue

        print(result)

    while True:
        print(msg_4)
        store_action = input()
        if store_action in ('y', 'n'):
            if store_action == 'y':
                if is_one_digit(result):
                    msg_index = 10
                    while msg_index <= 12:
                        print(MESSAGES[msg_index])
                        store_one_digit_action = input()
                        if store_one_digit_action == 'y':
                            msg_index += 1
                        elif store_one_digit_action == 'n':
                            break
                        else:
                            continue
                    if msg_index == 13:
                        memory = result
                else:
                    memory = result
            break
        else:
            continue

    while True:
        print(msg_5)
        continue_action = input()
        if continue_action in ('y', 'n'):
            break
        else:
            continue

    if continue_action == 'y':
        continue
    else:
        break
