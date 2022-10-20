import os
import time

pid = os.fork()

print(f'start run')

if pid == 0:
    print(f'父进程{os.getppid()}, 子进程{os.getpid()}')
else:
    print(f'父进程{os.getpid()}')

