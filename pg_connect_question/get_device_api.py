import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

SERVER_IP = '10.80.3.138'
SERVER_PORT = '8000'

test_api = '/api/v1/cedar/device/?status=busy'


def get_device_data():
    url = f'http://{SERVER_IP}:{SERVER_PORT}{test_api}'
    res = requests.get(url=url)
    if res.status_code == 200:
        return 1
    else:
        with open('error.log', 'a+') as e:
            e.write(res.content)
        return 2

def main():
    with ThreadPoolExecutor(max_workers=5) as t:
        obj_list = []
        for _ in range(1000):
            task = t.submit(get_device_data)
            obj_list.append(task)

        for feature in as_completed(obj_list):
            data = feature.result()
            print(data)


if __name__ == '__main__':
    main()

