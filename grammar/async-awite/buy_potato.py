import asyncio
import random
import time


class Potato():

    @classmethod
    def make(cls, num, *args, **kwargs):
        potatos = []
        for i in range(num):
            potatos.append(cls.__new__(cls))
        return potatos


class Tomato():

    @classmethod
    def make(cls, num, *args, **kwargs):
        tomatos = []
        for i in range(num):
            tomatos.append(cls.__new__(cls))
        return tomatos


potatos = Potato.make(5)
tomatos = Tomato.make(5)

async def take_tomato(num):
    count = 0
    while True:
        if len(tomatos) == 0:
            await tak_for_tomato()
        else:
            tomato = tomatos.pop()
            yield tomato
            count += 1
            if count == num:
                break


async def tak_for_tomato():
    await asyncio.sleep(random.random())
    tomatos.extend(Tomato.make(random.randint(1, 10)))


async def buy_tomato(num):
    basket = []
    async for i in take_tomato(num):
        basket.append(i)
        print(f'Got Tomato {id(i)}')


async def take_potato(num):
    count = 0
    while True:
        if len(potatos) == 0:
            # time.sleep(.1)
            await ask_for_potato()
        else:
            potato = potatos.pop()
            yield potato
            count += 1
            if count == num:
                break

async def ask_for_potato():
    await asyncio.sleep(random.random())
    potatos.extend(Potato.make(random.randint(1, 10)))

async def buy_potato(num):
    basket = []
    async for i in take_potato(num):
        basket.append(i)
        print(f'Got Potato {id(i)}')

# def buy_potato(num):
#     basket = []
#     for i in take_potato(num):
#         print(basket)
#         basket.append(i)
def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([buy_potato(10), buy_tomato(10)]))
    loop.close()


if __name__ == '__main__':
    main()
