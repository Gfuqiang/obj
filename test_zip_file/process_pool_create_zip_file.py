import multiprocessing, zipfile, os, time
from multiprocessing import pool, Lock
from tool.watch import func_time_watch


def create_process_poll():
    p = pool.Pool(multiprocessing.cpu_count())
    return p


@func_time_watch
def zip_file(file_path, zip_path):
    print(f'********** {os.getpid()} start run')
    with zipfile.ZipFile(zip_path, 'a') as z:
        z.write(file_path)
    print(f'********** {os.getpid()} end run')


def run():
    # 准备zip dir路径
    if not os.path.exists('./zip_dir'):
        os.mkdir('./zip_dir')

    # get pool instance
    p = create_process_poll()
    # 获取文件列表
    file_list = os.listdir('./file_dir')
    for file in file_list:
        p.apply_async(zip_file, args=(f'./file_dir/{file}', f'./zip_dir/test.zip'))
    p.close()
    p.join()
    print(f'====================:end')


class CreateZipFile():

    def __init__(self):
        self.p = pool.Pool(multiprocessing.cpu_count())
        self.file_path = os.listdir('./file_dir')
        self.zip_path = './zip_dir/test.zip'
        self.lock = Lock()

    @staticmethod
    def zip_file_func(self, file, zip_path):
        self.lock.acquire()
        print(f'********** {os.getpid()} start run')
        with zipfile.ZipFile(zip_path, 'a') as z:
            z.write(file)
        print(f'********** {os.getpid()} end run')
        self.lock.release()

    def run(self):
        func_name = self.zip_file_func.__name__
        for file in self.file_path:
            self.p.apply_async(func_name, args=(f'./file_dir/{file}', self.zip_path))
        self.p.close()
        self.p.join()


if __name__ == '__main__':
    print(f'Father pid: {os.getgid()}')
    c = CreateZipFile()
    c.run()
    c.p.close()
    c.p.join()
    print(f'================ end')
