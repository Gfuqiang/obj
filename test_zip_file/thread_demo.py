import threading, time, random


def run(a, b):
    time.sleep(random.randint(1, 3))
    print(a, b)


if __name__ == '__main__':
    print(f'===================== start')
    t = threading.Thread(target=run, args=(1, 2))
    t1 = threading.Thread(target=run, args=(3, 4))
    t.start()
    t1.start()
    print(t1.is_alive())
    t.join()
    t1.join()
    print(t1.is_alive())
    print(f'===================== end')