import os


def create_file_func(file_name, size):
    with open(file_name, 'w') as f:
        f.write((f'Hello 你好' * 100 + '\n') * 100000)


def main(file_num):
    if not os.path.exists('./file_dir'):
        os.mkdir('./file_dir')
    for i in range(file_num):
        create_file_func(f'./file_dir/{i}.txt', 100)


if __name__ == '__main__':
    main(3)