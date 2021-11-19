import os,zipfile, multiprocessing
from multiprocessing import Value


def unzip(zip_path, unzip_path):
    if not os.path.exists(unzip_path):
        os.mkdir(unzip_path)
    z = zipfile.ZipFile(zip_path, 'r', compression=zipfile.ZIP_DEFLATED)
    z.extractall(unzip_path, z.namelist())
    # for file in z.namelist():
    #     print(file)
    #     z.extract(file, unzip_path)
    z.close()


def unzip_func(parameter):
    v, file = parameter
    v = v.value()
    v.extract(file, './unzip_dir')


def unzip_process(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as z:
        v = Value('i', z)
        z.namelist()
        with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
            multiple_res = [pool.apply_async(unzip_func, [(v, file)]) for file in z.namelist()]
            for i in multiple_res:
                print(i.get(timeout=5))


if __name__ == '__main__':
    # unzip('./zip_dir/test.zip', './unzip_dir')
    unzip_process('./zip_dir/test.zip')