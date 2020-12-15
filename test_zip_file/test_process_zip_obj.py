"""
测试多进程中zip是否是同一个句柄
"""
import zipfile, os
from multiprocessing import Process, Lock
from tool.watch import func_time_watch


def create_lock():
    lock = Lock()
    return lock


@func_time_watch
def run_zip(file_path):
    lock = create_lock()
    print(f'lock id: {id(lock)}')
    lock.acquire()
    print(f'process id: {os.getpid()}, {file_path}')
    if not os.path.exists('./zip_dir'):
        os.mkdir('./zip_dir')
    with zipfile.ZipFile('./zip_dir/test.zip', 'a', compression=zipfile.ZIP_DEFLATED) as z:
        z.write(file_path)
    print(f'{os.getpid()} complete')
    lock.release()


def read_file(file_path):
    with open(file_path, 'r') as f:
        print(f'{os.getpid()} === {f.readline()}')


def main():
    p1 = Process(target=run_zip, args=('./file_dir/0.txt',))
    p2 = Process(target=run_zip, args=('./file_dir/1.txt',))
    p3 = Process(target=run_zip, args=('./file_dir/2.txt',))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    # run_zip('./file_dir/0.txt')
    # run_zip('./file_dir/1.txt')
    # run_zip('./file_dir/2.txt')
    print(f'run complete')

if __name__ == '__main__':
    main()