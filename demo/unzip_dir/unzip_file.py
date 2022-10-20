import zipfile, pathlib
import hashlib

p = pathlib.Path('.')
file_name = '闪屏测试用例1.zip'


def unzip_file():
    with zipfile.ZipFile(f'/Users/fq/Desktop/{file_name}', 'r') as z:
        z.extractall(p / 'zip_file_dir')


def compare_file_md5(file_list):
    for file in file_list:
        with open(file, 'rb') as f:
            print(hashlib.md5(f.read()).hexdigest())


if __name__ == '__main__':
    p = pathlib.Path.home() / "Desktop"
    file_name = p / '闪屏测试用例.zip'
    file_name1 = p / '闪屏测试用例1.zip'
    # compare_file_md5([file_name, file_name1])
    try:
        with zipfile.ZipFile(file_name, 'r', compression=zipfile.ZIP_BZIP2) as f:
            file_name = f.testzip()
            print(file_name)
    except zipfile.BadZipFile as e:
        print(e)

    if zipfile.is_zipfile(file_name1):
        print(111)
    else:
        print(222)
