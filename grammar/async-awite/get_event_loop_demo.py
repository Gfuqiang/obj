import asyncio, time


def hello_world(loop):
    print('Hello World')
    loop.stop()


async def download_url(url):
    await asyncio.sleep(2)
    print(f'download url success: {url}')

if __name__ == '__main__':
    start_time = time.time()
    # 创建事件循环
    loop = asyncio.get_event_loop()
    all_task = [download_url('http//:127.0.0.1:8000') for _ in range(10)]
    # 将任务函数放入循环中
    loop.run_until_complete(asyncio.wait(all_task))
    print(time.time() - start_time)

    # Schedule a call to hello_world()
    # loop.call_soon(hello_world, loop)
    #
    # # Blocking call interrupted by loop.stop()
    # loop.run_forever()
    # loop.close()
