from pathlib import Path


def get_file_path(file_name):
    p = Path(f'./statistic_file/{file_name}')
    return p


if __name__ == '__main__':
    p = get_file_path('big_file_test.txt')
    with open(p, 'r') as f:
        # print(f.readlines())
        print(f.read())