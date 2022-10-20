"""
偷水滴
"""
import requests, time, os, sys

num = 1     # 别人浇水搜索轮数
number_rounds = 3  # 查找次数
sleep_time = 2

headers = {
    'Host': 'e-mall.dfpv.com.cn',
    'Content-Type': 'application/json',
    'Origin': 'https://e-mallh5.dfpv.com.cn',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.16(0x18001041) NetType/WIFI Language/zh_CN miniProgram',
    'Referer': 'https://e-mallh5.dfpv.com.cn/',
    'token': 'GRAIN:TOKEN:b9424853772e43e',
}


def handle_request(url, body):
    res = requests.post(url, headers=headers, json=body)
    return res


def get_random_user():
    url = 'https://e-mall.dfpv.com.cn/web/mp/forest/randomUser'
    body = {
        "activityId": "402",
        "userId": 7052724
    }
    res = handle_request(url, body)
    res_data = res.json()
    if res_data.get('errno') == 200:
        user_list = res_data.get('data')
        return user_list
    else:
        print(f"哎呀获取随机用户出错了：{res_data}")


def get_have_water_for_user(user_list, my_water_num):
    """
    让有水的人给自己浇水
    :return:
    """
    print(f'user_list len: {len(user_list)}')
    get_good_user = [
        user_info.get('userId')
        for user_info in user_list
        if user_info.get('balance') > my_water_num
    ]
    if get_good_user:
        print(f'good_user: {get_good_user}')
    else:
        print(f'**************没有一个比我水多，没有一个能给浇水的，呜呜呜~~')
    return get_good_user


def get_can_steal_user(user_list):
    print(f'user_list len: {len(user_list)}')
    get_good_user = [user_info.get('userId') for user_info in user_list if user_info.get('isStealWater') == 1]
    if get_good_user:
        print(f'good_user: {get_good_user}')
    else:
        print(f'**************获取可偷用户获取了个寂寞~~')
    return get_good_user


def people_get_oneself_water(user_id_list):
    url = 'https://e-mall.dfpv.com.cn/web/mp/forest/warting'
    for user_id in user_id_list:
        time.sleep(1.5)
        body = {
            "userId": "7052724",
            "activityId": "402",
            "operateUserId": user_id
        }
        res = handle_request(url, body)
        res_data = res.json()
        if res_data.get('errno') == 200 and res_data:
            print(f'{user_id}: 浇水成功，谢谢~~ {res_data.get("errmsg")}')
        else:
            print(f"{user_id}: 给我浇水失败了，原因：{res_data}")


def get_user_water(user_id_list):
    url = 'https://e-mall.dfpv.com.cn/web/mp/forest/waterIndex'
    result = {}
    for user_id in user_id_list:
        water_id_list = []
        body = {
            "activityId": "402",
            "userId": user_id
        }
        res = handle_request(url, body)
        res_data = res.json()
        if res_data.get('errno') == 200 and res_data.get('data'):
            water_id_list = [water.get('id') for water in res_data.get('data')]
            if water_id_list:
                water_id_list.extend(water_id_list)
        if water_id_list:
            result[user_id] = water_id_list
    if result:
        print(f'===========还是有一点收获的哈')
        print(f'water_id_list: {result}')
    else:
        print(f'===========获取水滴获取了个寂寞~~~')
    return result


def steal_user_water(user_water_data):
    """
    user_water_data:
    {user_id: [water_list]}
    err:
    {
    "success": false,
    "data": null,
    "errno": 402,
    "errmsg": "能量值太低不能偷取"
    }
    :return:
    """
    url = 'https://e-mall.dfpv.com.cn/web/mp/forest/getWater'
    for user_id in user_water_data.keys():
        for water_id in user_water_data.get(user_id, []):
            body = {
                "id": water_id,
                "userId": user_id,
                "operateUserId": "7052724"  # 自己id
            }
            res = handle_request(url, body)
            res_data = res.json()
            if res_data.get('errno') == 200 and res_data:
                print(f'************收获了:{res_data.get("errmsg")}')
            elif res_data.get('errno') == 402:
                break
            else:
                print(f'************遇到未知错误:{res_data}')
                break


def handle(url, body):
    res = requests.post(url, headers=headers, json=body)
    return res


def get_oneself_water():
    # get water list
    get_water_url = 'https://e-mall.dfpv.com.cn/web/mp/forest/waterIndex'
    use_up_water_url = 'https://e-mall.dfpv.com.cn/web/mp/forest/getWater'
    body = {
        "activityId": "402",
        "userId": 7052724
    }
    res = handle(get_water_url, body)
    res = res.json()
    if res.get('errno') == 200 and res and res.get('data'):
        for water_dict in res.get('data'):
            body1 = {
                "id": water_dict.get("id"),
                "userId": 7052724,
                "operateUserId": ""
            }
            res = handle(use_up_water_url, body1)
            res = res.json()
            if res.get('errno') == 200:
                print(f'**************收取水滴成功了: {water_dict.get("id")}')
            else:
                print(f'呀！！！收取水滴失败,返回的是：{res}')
    else:
        print(f'自己没有可以收取的水滴，洗洗睡了: {res}')


def steal_water_func():
    # 获取用户

    for i in range(number_rounds):
        time.sleep(sleep_time)
        user_list = get_random_user()
        user_list = get_can_steal_user(user_list)
        # 有用户可偷
        if user_list:
            user_water_data = get_user_water(user_list)
            steal_user_water(user_water_data)


def get_my_water_num():
    # 获取自己水滴数
    pass


def get_other_user_water():
    # 让比我水多的人给我浇水
    for i in range(num):
        time.sleep(sleep_time)
        user_list = get_random_user()
        user_list = get_have_water_for_user(user_list)
        people_get_oneself_water(user_list)


def main():
    # 偷水滴
    print(f'*' * 50 + '\n' + f'偷水滴开始')
    steal_water_func()
    # 让有水的人给自己浇水
    # print(f'*' * 50 + '\n' + f'别人给我浇水')
    # get_other_user_water()
    # print(f'*' * 50 + '\n' + f'收自己水滴')
    # 7点收自己的水滴
    # get_oneself_water()


if __name__ == '__main__':
    main()
