import time


def start_strongman(name: str, power: int):
    quantity_ball = 5
    print(f'Силач {name} начал соревнования.')
    i = -1
    while i < quantity_ball - 1:
        i += 1
        time.sleep(1 / power)
        print(f'Силач {name} поднял {quantity_ball - i} шар')
    print(f'Силач {name} закончил соревнования.')


def start_tournament():
    print('Start')
    start_strongman('Василий', 3)
    start_strongman('Явдат', 1)
    start_strongman('Силантий', 2)
    print('Finish')


start = time.time()
start_tournament()
finish = time.time()

print(f'\nWorking time = {finish - start} second')
