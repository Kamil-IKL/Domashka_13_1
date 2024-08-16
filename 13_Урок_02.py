import time
import asyncio

async def get_temp():
    print('Первое показание')
    # time.sleep(2)
    await asyncio.sleep(2)
    print('25 С')                              # Температура

async def get_pres():
    print('Второе показание')
    # time.sleep(4)
    await asyncio.sleep(4)
    print('101 kPa')                            # Давление


async def main():
    print('Старт')                              # Время начало работы
    task_1 = asyncio.create_task(get_temp())
    task_2 = asyncio.create_task(get_pres())
    await task_1
    await task_2
    print('Финиш')                              # Время конца работы

start = time.time()
asyncio.run(main())
finish = time.time()


print(f'Working time (время работы) = {finish - start} seconds')
