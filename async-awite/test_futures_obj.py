import concurrent.futures
import requests
import time

def download_one(url):
    try:
        ret = requests.get(url)
        print(f'Read {len(ret.content)} from {url}')
    except Exception as e:
        return f'Error: {e}'


def download_all(sites):

    to_do = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for site in sites:
            future = executor.submit(download_one, site)
            to_do.append(future)

        for future in concurrent.futures.as_completed(to_do):
            print(future.result())


if __name__ == '__main__':
    sites = [
        'https://blog.csdn.net/u011519550/article/details/83413318',
        'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%A4%A7%E4%BC%97%E7%82%B9%E8%AF%84&fenlei=256&rsv_pq=bfd927be0009031f&rsv_t=28eaIv1scDPvbgSm5yOPE6D%2FJJICeVDPNnolq8qxJT5k%2BoWIWdHkWE3zkuw&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=18&rsv_sug1=17&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=%25E5%25A4%25A7%25E4%25BC%2597%25E7%2582%25B9%25E8%25AF%2584&rsp=5&inputT=5801&rsv_sug4=10718',
        'http://10.0.0.57:8251/root/reef/pipelines'
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    use_time = end_time - start_time
    print(f'使用时间为：{use_time}')

