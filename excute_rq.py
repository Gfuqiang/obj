"""
健康植物园
POST /api/add_growth_value HTTP/1.1
Host: xinruismzd-isv.isvjcloud.com
Accept: application/json, text/plain, */*
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
Accept-Encoding: gzip, deflate, br
Referer: https://xinruismzd-isv.isvjcloud.com/healthy-plant2021/?channel=ddjkicon&lng=116.237826&lat=39.89491&sid=57e2daf7d7f5b5add7df69d85cf3770w&un_area=1_2806_54713_0
Content-Type: application/json
Origin: https://xinruismzd-isv.isvjcloud.com
User-Agent: Mozilla/5.0 (Linux; Android 10; TAS-AN00 Build/HUAWEITAS-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045713 Mobile Safari/537.36
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC94aW5ydWlzbXpkLWlzdi5pc3ZqY2xvdWQuY29tXC9hcGlcL2F1dGgiLCJpYXQiOjE2MzcyODgyMTksImV4cCI6MTYzNzMzMTQxOSwibmJmIjoxNjM3Mjg4MjE5LCJqdGkiOiJTS20xZ0t3ZDRmZUpnajJ5Iiwic3ViIjoibGRDZHhzdjhHM2pra3I4ZENTZGF0SGQ5RWpKV0JmRWZ4UC1kZHVrcnotVSIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.-2yzeCf5ZcE4o_GQpzTZQrvV8QYG6DgwJo7VWUXZZ8A
cache-control: no-cache
Postman-Token: bd8f09e1-6c33-4de5-acc3-b73ac931b201
{
	"plant_id": 9642
}------WebKitFormBoundary7MA4YWxkTrZu0gW--
"""
import json, time

import requests


def execute():

    url = 'https://xinruismzd-isv.isvjcloud.com/api/add_growth_value'

    Authorization = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC94aW5ydWlzbXpkLWlzdi5pc3ZqY2xvdWQuY29tXC9hcGlcL2F1dGgiLCJpYXQiOjE2Mzc1Nzk1MzEsImV4cCI6MTYzNzYyMjczMSwibmJmIjoxNjM3NTc5NTMxLCJqdGkiOiJub2tOcUsweG5KYU9EVkFDIiwic3ViIjoibGRDZHhzdjhHM2pra3I4ZENTZGF0SGQ5RWpKV0JmRWZ4UC1kZHVrcnotVSIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.CMKtOL0yJTTM8XFRfB1xUH7sKHnzI5I-jtMj9frNdV8'

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://xinruismzd-isv.isvjcloud.com/healthy-plant2021/?channel=ddjkicon&lng=116.237826&lat=39.89491&sid=57e2daf7d7f5b5add7df69d85cf3770w&un_area=1_2806_54713_0',
        'Content-Type': 'application/json',
        'Origin': 'https://xinruismzd-isv.isvjcloud.com',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; TAS-AN00 Build/HUAWEITAS-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045713 Mobile Safari/537.36',
        'Authorization': Authorization

    }

    for i in range(2):
        time.sleep(2)
        data = json.dumps({"plant_id": 9642})
        response = requests.post(url=url, headers=headers, data=data)
        try:
            res = response.json()
            if isinstance(res, dict):
                res_data = res
            else:
                res_data = json.loads(res)

            status_code = res_data.get('status_code', None)
            message = res_data.get('message', None)
            plant_info = res_data.get('plant_info', None)
            # 判断是否添加能量成功
            if status_code:
                print(f'stauts_code: {status_code}')
            else:
                print(f'status_code 没有获取到，res是{res}')
                exit(-3)
            if status_code == 422 or message == '今日充值次数达到上限':
                print(f'今日充值次数达到上限')
                exit(-2)
            elif plant_info:
                coins = plant_info.get('coins', None)
                print(f'已填充能量数为：{coins}')
            else:
                print(f'未知 response 数据可能接口返回值变更了或token已经过期了，请检查！！！')
        except Exception as e:
            print(f'response json encode eroor: {e}')
            exit(-1)

if __name__ == '__main__':
    execute()


