from datetime import timedelta

from telethon import TelegramClient, events

# Use your own values from my.telegram.org
api_id = 19797628
api_hash = 'b18aaf49d0f6846faacac588235ed074'

# The first parameter is the .session file name (absolute paths allowed)
client = TelegramClient('s_name', api_id, api_hash, proxy=("socks5", '127.0.0.1', 7890))

data_list = [
    "/ddfactory T0225KkcRBoQo1bWdk7ykfYLdgCjVWnYaS5kRrbA&T0156LgyGU9HolLVJhsCjVWnYaS5kRrbA",
    "/farm b5404a3264314c22ab808f50ec271b91&1a2b8dc7cff147d79c0919ee7ae49288&f6faa12ca56645f78fdcbfea399372b8",
    "/pet MTE1NDY3NTIwMDAwMDAwNTA1NjAwNTM=&MTE1MzEzNjI2MDAwMDAwMDUwNTAwMDg1&MTEzMzI1MTE4NTAwMDAwMDA1MzYyMjEwOQ==",
    "/sgmh T0225KkcRBoQo1bWdk7ykfYLdgCjVQmoaT5kRrbA&T0156LgyGU9HolLVJhsCjVQmoaT5kRrbA&T0116LwkFxgb81UCjVQmoaT5kRrbA",
    "/jxfactory cuvd07uym9nyyqUCur72MQ==&dPWHtvxRmGzBWkLlpByibg==&ZHzRW0_U8rkmFEyJOnFqRg==",
    "/bean e7lhibzb3zek26bfqczp37w4atyph6yu7tt6aiy&vihbcbm6khscl7e5fmofumd4oa&k2i62r2ppodrp6r4n3r6englti",
    "/health T0225KkcRBoQo1bWdk7ykfYLdgCjVfnoaW5kRrbA&T0156LgyGU9HolLVJhsCjVfnoaW5kRrbA&T0116LwkFxgb81UCjVfnoaW5kRrbA"
    # "/bind fqgg6261",
    # "/bind fuqiang6261",
    # "/bind jd_449f21fd65112"
]


async def main(data_list):
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    # print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    # 获取所有对话及id
    # async for dialog in client.iter_dialogs():
    #     print(dialog.name, 'has ID', dialog.id)
    # 测试定时任务
    # await client.send_message('me', 'Walk the dog',
    #                           schedule=timedelta(minutes=1))
    # await client.send_message('me', '1111111')
    print(f'my_phone: {me.phone}')
    for data in data_list:
        try:
            await client.send_message(5479559602, data)
        except Exception as e:
            print(e)
        else:
            print(f'{data.split(" ")[0]} 成功')
    # You can print all the dialogs/conversations that you are part of:
    # async for dialog in client.iter_dialogs():、
    # 发送share code码
    # message = await client.send_message(2099192540, '/ddfactory T0225KkcRBoQo1bWdk7ykfYLdgCjVWnYaS5kRrbA')

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main(data_list))