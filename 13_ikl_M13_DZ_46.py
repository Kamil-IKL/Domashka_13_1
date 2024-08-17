import time
import asyncio

"""
cначала написал код (файл "probe") потом здесь ассинхронизировал
"""


async def start_strongman(name: str, power: int):
    quantity_ball = 5
    print(f'Силач {name} начал соревнования.')
    i = -1
    while i < quantity_ball - 1:
        i += 1
        # time.sleep(1 / power)
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {quantity_ball - i} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    print('Start')
    task_1 = asyncio.create_task(start_strongman('Василий', 3))
    task_2 = asyncio.create_task(start_strongman('Явдат', 1))
    task_3 = asyncio.create_task(start_strongman('Силантий', 2))
    await task_1
    await task_2
    await task_3
    print('Finish')



start = time.time()
asyncio.run(start_tournament())
finish = time.time()

print(f'\nWorking time = {finish - start} second')
