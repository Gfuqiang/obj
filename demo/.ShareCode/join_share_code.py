import os
from pathlib import Path, PosixPath

get_code_file_name = ['Bean.log', 'Fruit.log', 'DreamFactory.log', 'Pet.log', 'Health.log',
                      'JdFactory.log', 'Sgmh.log']


def get_path():
    dir_path = Path('.')
    return [file for file in dir_path.glob('**/*.log') if file.is_file()]


def read_file_content(path: PosixPath):
    code_list = []
    with path.open() as f:
        contents = f.readlines()
        for content in contents:
            content = content.rstrip('\n')
            if content.startswith(f'My{path.stem}'):
                # if content.startswith(f'MyDreamFactory'):
                #     share_code = content.split("'")[1]
                # else:
                share_code = content.split('=', maxsplit=1)[1].strip("'")

                if share_code:
                    code_list.append(share_code)
    return '&'.join(code_list)


def join_code(path_list):
    global get_code_file_name
    for path_obj in path_list:
        if path_obj.name in get_code_file_name:
            share_code_str = read_file_content(path_obj)
            if path_obj.name == 'Bean.log':
                print(f'/bean {share_code_str}')
            elif path_obj.name == 'Fruit.log':
                print(f'/farm {share_code_str}')
            elif path_obj.name == 'DreamFactory.log':
                print(f'/jxfactory {share_code_str}')
            elif path_obj.name == 'Pet.log':
                print(f'/pet {share_code_str}')
            elif path_obj.name == 'Health.log':
                print(f'/health {share_code_str}')
            elif path_obj.name == 'JdFactory.log':
                print(f'/ddfactory {share_code_str}')
            elif path_obj.name == 'Sgmh.log':
                print(f'/sgmh {share_code_str}')
            else:
                print(f'出现一个异类，文件名称:{path_obj.name}')


if __name__ == '__main__':
    path_obj_list = get_path()
    join_code(path_obj_list)



