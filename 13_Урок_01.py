import time
import asyncio
async def notification():
    time.sleep(10)
    print('До доставки осталось 10 минут')




async def main():
    task = asyncio.create_task(notification())
    print('Собираемся в поездку')
    print('Едим')

# движок запуска асинхронной функции
asyncio.run(main())
