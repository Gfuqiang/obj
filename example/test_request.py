import threading, requests, os
from concurrent.futures import ThreadPoolExecutor, as_completed


def request_reef(item):
    s = requests.session()
    s.keep_alive = False
    url = 'http://10.80.5.138:8000/media/job_res_file_export/job-2e47bd0a-d65c-93ee-b414-2df19db5e39c.zip'
    res = requests.get(url, timeout=60)
    dir_name = os.path.join((os.path.dirname(os.path.abspath(__file__))), 'zip')
    print(f'run: {item}')
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(f'{dir_name}/file.zip{item}', 'wb+') as f:
        for chunk in res.iter_content(chunk_size=1024):
            f.write(chunk)
    # print(res.text)


def main():
    with ThreadPoolExecutor(max_workers=800, thread_name_prefix='my-') as executor:
        features = [executor.submit(request_reef, i) for i in range(800)]
        for feature in as_completed(features):
            print(feature.result())
        # features = executor.map(request_reef, [i for i in range(10)])
        # print(threading.enumerate())


if __name__ == '__main__':

    # for i in range(50):
    #     t = threading.Thread(target=request_reef, args=(i,))
    #     t.start()
    #     t.join()
    # request_reef(1)
    main()


