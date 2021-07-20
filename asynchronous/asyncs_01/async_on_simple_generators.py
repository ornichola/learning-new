import time


QUEUE = []


def counter():
    count = 0
    while True:
        print(count)
        count += 1
        yield


def printer():
    count = 0
    while True:
        if count % 3 == 0:
            print('Bang!')
        count += 1
        yield


def main():
    while True:
        gen = QUEUE.pop()
        next(gen)
        QUEUE.append(gen)
        time.sleep(1)


if __name__ == '__main__':
    gen_01 = counter()
    QUEUE.append(gen_01)
    gen_02 = printer()
    QUEUE.append(gen_02)
    main()
