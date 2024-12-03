"""
测试解压400M 以上压缩包
"""
import zipfile, os
from pathlib import Path

dir = os.path.dirname(__file__)
unzip_dir = os.path.join(dir, '../unzip_dir')


def unzip_big_file(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as f:
        f.extractall(unzip_dir)


def unzip_big_file_ex(zip_file):
    zip_obj = zipfile.ZipFile(zip_file, 'r', zipfile.ZIP_DEFLATED, allowZip64=False)
    extractfile = zip_obj.namelist()
    for file in extractfile:
        zip_obj.extract(file, unzip_dir)


if __name__ == '__main__':
    p = Path('/')
    # job-export-其他1-44.zip
    q = p / 'Users' / 'fq' / 'Desktop'
    zip_file_path = os.path.join(q, 'job-export-其他1-44.zip')
    # unzip_big_file(zip_file_path)
    # unzip_big_file_ex(zip_file_path)
    zip_dir_list = [i for i in Path(unzip_dir).iterdir() if i.is_dir()]
    print(len(zip_dir_list))
    print(Path().cwd())

    # 获取目录名称
    print(os.listdir(Path().cwd()))
    # for i in os.listdir(Path().cwd()):
        # print(i)

    print([i.name for i in Path().cwd().iterdir() if i.is_dir()])