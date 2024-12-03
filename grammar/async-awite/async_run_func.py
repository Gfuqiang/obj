import asyncio


async def work1():
    print('start run work1')
    await asyncio.sleep(1)
    print('end run work1')


async def work2():
    print('start run work2')
    await asyncio.sleep(2)
    print('end run work2')


async def main():
    task1 = asyncio.create_task(work1())
    task2 = asyncio.create_task(work2())
    print('before work')
    await task1
    print('await task1')
    await task2
    print('await task2')


if __name__ == '__main__':
    # python 3.7 才有run方法
    asyncio.run(main())

