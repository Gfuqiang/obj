import zipfile, os, multiprocessing
from tool.watch import func_time_watch
from multiprocessing import Queue


class MyZipFile(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_Singleton'):
            cls._Singleton = super().__new__(cls)
        return cls._Singleton

    def __init__(self):
        self.z_obj = zipfile.ZipFile('./zip_dir/test.zip', 'w', compression=zipfile.ZIP_DEFLATED)

    @staticmethod
    def get_zip_instance():
        return zipfile.ZipFile('./zip_dir/test.zip', 'w', compression=zipfile.ZIP_DEFLATED)


z = MyZipFile()

# Q
q = Queue(5)
q.put(z)


@func_time_watch
def zip_file(zip_file_name, file_dir_name):

    pool = create_process_pool()
    file_list = os.listdir(file_dir_name)
    cpu_num = multiprocessing.cpu_count()
    # 按cpu count切分file list
    parameter_list = []

    if len(file_list) < cpu_num:
        for i in range(len(file_list)):
            parameter_list.append([1, file_list[i:i+1], file_dir_name])
    for r in pool.imap_unordered(pack_parameter, parameter_list):
        print(r)


def create_zpi_file(file_name, file_list, dir_name):
    print(f'Process run, pid:{os.getpid()}')
    # z = MyZipFile()
    # print(id(z))
    try:
        z = q.get()
        print(id(z))
        z_obj = z.z_obj
        for f in file_list:
            z_obj.write(dir_name + os.sep + f)
        z_obj.close()
    except Exception as e:
        print(f'get q data error: {e}')
        exit(1)


def pack_parameter(parameter):
    create_zpi_file(parameter[0], parameter[1], parameter[2])


def create_process_pool():
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    return pool


def main():
    file_dir = './file_dir'
    zpi_dir_path = './zip_dir'
    if not os.path.exists(zpi_dir_path):
        os.mkdir(zpi_dir_path)
    # run zip
    zip_file(f'{zpi_dir_path}/test.zip', file_dir)


if __name__ == '__main__':
    main()
    # z1 = MyZipFile()
    # z2 = MyZipFile()
    # print(id(z1))
    # print(id(z2))
    # print
    # print(z1.name)
    # print(z1.a)
    # print(z1.z_obj)
    # z2 = ZipFile()
    # print(id(z1))
    # print(id(z2))
    # print(z1.get_zip_instance())