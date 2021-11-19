import zipfile
import threading
import os, time


class MyZip():

    def __new__(cls, *args, **kwargs):
        print(args)
        if not hasattr(cls, '_Single'):
            cls._Single = zipfile.ZipFile(args[0], 'a', compression=zipfile.ZIP_DEFLATED)
        return cls._Single

    @classmethod
    def close_file_conn(cls):
        cls._Single.close()

    def __init__(self, zip_path, file_path):
        self.file_path = file_path
        self.zip_path = zip_path
        self.lock = threading.Lock()

    def __call__(self, *args, **kwargs):
        print(f'lock id{id(self.lock)}')
        is_true = self.lock.acquire()
        print(f'get lock: {is_true}')
        print(f'开始执行 ****************')
        if os.path.exists(self.zip_path):
            print(f'append')
            with zipfile.ZipFile(self.zip_path, 'a', compression=zipfile.ZIP_DEFLATED) as z:
                print(id(z))
                z.write(self.file_path)
        else:
            with zipfile.ZipFile(self.zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as f:
                print(id(f))
                f.write(self.file_path)
        self.lock.release()
        print(f'release lock')


lock = threading.Lock()


def package(file_path, zip_path):
    m1 = MyZip(zip_path)
    print(f'z obj id: {id(m1)}')
    print(f'lock id: {id(lock)}')
    is_true = lock.acquire()
    print(f'get lock: {is_true}')
    m1.write(file_path)
    lock.release()
    print(f'release lock')


class Mylock():

    def __new__(cls, *args, **kwargs):
        print(args)
        return cls


def hello(x, y):
    print(x + y)


def timer_func():
    t = threading.Timer(5, hello, args=(1, 1))
    t.start()

if __name__ == '__main__':

    t = threading.Thread(target=timer_func)
    t.start()
    print(111)

    #-----------------------
    # m1 = MyZip('./zip_dir/test.zip')
    # m2 = MyZip('./zip_dir/test1.zip')
    # print(id(m1))
    # print(id(m2))
    #
    # # create thread
    # t1 = threading.Thread(target=package, args=('./file_dir/0.txt', './zip_dir/test.zip'))
    # t2 = threading.Thread(target=package, args=('./file_dir/1.txt', './zip_dir/test.zip'))
    # t1.start()
    # t2.start()
    # # # print(t1.is_alive())
    # # # print(t2.is_alive())
    # t1.join()
    # t2.join()
    # MyZip.close_file_conn()
    # print(t1.is_alive())
    # print(t2.is_alive())









