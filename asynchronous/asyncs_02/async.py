# # synchronous
#
# import time
#
#
# def find_divisible(in_range, div_by):
#     print(f'Finding nums in range {in_range} divisible by {div_by}')
#     located = []
#     for i in range(in_range):
#         if i % div_by == 0:
#             located.append(i)
#     print(f'Done w/ nums in range {in_range} divisible by {div_by}')
#     return located
#
#
# def main():
#     find_divisible(500_000_000, 333)
#     find_divisible(500_000, 34_113)
#     find_divisible(100_052, 3_210)
#     find_divisible(500, 3)
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#     main()
#     print(f'Took out {round(time.time() - start_time, 2)}s')


# asynchronous

import asyncio


async def find_divisible(in_range, div_by):
    print(f'Finding nums in range {in_range} divisible by {div_by}')
    located = []
    for i in range(in_range):
        if i % div_by == 0:
            located.append(i)
        if i % 50_000 == 0:
            await asyncio.sleep(0.00001)
    print(f'Done w/ nums in range {in_range} divisible by {div_by}')
    return located


async def main():
    divs1 = loop.create_task(find_divisible(500_000_000, 333))
    divs2 = loop.create_task(find_divisible(500_000, 34_113))
    divs3 = loop.create_task(find_divisible(100_052, 3_210))
    divs4 = loop.create_task(find_divisible(500, 3))
    await asyncio.wait([divs1, divs2, divs3, divs4])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
