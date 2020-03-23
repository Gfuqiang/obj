import asyncio
import os

os.path.abspath(__file__)
obj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
media = os.path.join(obj_path, "media_file")


async def create_file(file_num):
    if not os.path.exists(media):
        os.mkdir(media)
    for i in range(file_num):
        async with open(f'{os.path.join(obj_path, "media_file", str(i) + ".txt")}', 'w') as file:
            file.write('11111')

async def get_file_name_list():
    if os.path.exists(media):
        file_name_list = os.listdir(media)
        print(file_name_list)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather([create_file(100), get_file_name_list()]))


if __name__ == '__main__':
    main()