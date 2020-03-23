import asyncio
import time


async def computer(x, y):

    # result = await computer_subtraction(4,3)
    # print(result)
    await asyncio.sleep(8.0)
    print(f'computer count')
    return x + y

async def computer_subtraction(x, y):

    await asyncio.sleep(5.0)
    print(f'computer subtraction')
    return x - y


async def print_some(x, y):
    result, result_subtraction = await asyncio.gather(computer(x, y), computer_subtraction(4,3))
    # result_subtraction = await computer_subtraction(4, 3)
    # result = await computer(x, y)
    print(f'result: {result}')
    print(f'result: {result_subtraction}')


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([print_some(4,3)])) # run_until_complete 是一个阻塞的方法
    loop.close()

if __name__ == '__main__':
    start_time = time.time()
    main()
    print(f'use time {time.time() - start_time}')
