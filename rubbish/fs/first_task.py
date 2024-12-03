"""
卡片签到，分享
水签到

"""
import requests, time

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


def handle(url, body):
    res = requests.post(url, headers=headers, json=body)
    return res


def handle_request(url, body):
    time.sleep(0.5)
    res = requests.post(url, headers=headers, json=body)
    return res


def get_request(url):
    res = requests.get(url, headers=headers)
    return res


def card_clock():
    card_clock_url = 'https://e-mall.dfpv.com.cn/web/mp/wuFu/clock'
    body = {"activityId": "301"}
    res = handle(card_clock_url, body)
    print(res.json())


def card_share():
    card_clock_url = 'https://e-mall.dfpv.com.cn/web/mp/wuFu/share'
    body = {"activityId": "301"}
    res = handle(card_clock_url, body)
    print(res.json())


def water_clock():
    water_clock_url = 'https://e-mall.dfpv.com.cn/web/mp/forest/clock'
    body = {
        "activityId": "402",
        "userId": 7052724
    }
    res = handle(water_clock_url, body)
    print(res.json())


def water_share():
    card_clock_url = 'https://e-mall.dfpv.com.cn/web/mp/forest/share'
    for i in range(5):
        time.sleep(1.5)
        body = {"activityId": "402", "userId": 7052724}
        res = handle(card_clock_url, body)
        print(res.json())


def glance_water():
    # 浏览得水滴
    url = 'https://e-mall.dfpv.com.cn/web/mp/footprint/addPoint'
    for i in range(3):
        time.sleep(1)
        body1 = {
            "userId": 7052724,
            "position": 101  # 浏览爱车页面
        }
        body2 = {
            "userId": 7052724,
            "position": 4
        }
        res = handle(url, body1)
        print(f'++++++浏览101:{res.json()}')
        time.sleep(1.5)
        res = handle(url, body2)
        print(f'======浏览4:{res.json()}')


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
                "id": water_dict.get('id'),
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
        print(f'没有可以收取的水滴，洗洗睡了: {res}')


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
        return []


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


def people_get_oneself_water(user_id_list):
    url = 'https://e-mall.dfpv.com.cn/web/mp/forest/warting'
    watering_num = 0
    for user_id in user_id_list:
        time.sleep(0.5)
        body = {
            "userId": "7052724",
            "activityId": "402",
            "operateUserId": user_id
        }
        res = handle_request(url, body)
        res_data = res.json()
        if res_data.get('errno') == 200 and res_data:
            print(f'{user_id}: 浇水成功，谢谢~~ {res_data.get("errmsg")}')
            watering_num += 1
        else:
            print(f"{user_id}: 给我浇水失败了，原因：{res_data}")
    return watering_num


def get_my_water_num():
    url = 'https://e-mall.dfpv.com.cn/web/mp/forest/myWork?activityId=402&userId=7052724'
    res = get_request(url)
    res_data = res.json()
    if res_data.get('errno') == 200:
        return res_data.get('data').get('score')
    return 0


def author_for_me_water():
    """比我水多的给我浇水"""
    watering_num = 0
    # 获取我的水滴数
    my_water_num = get_my_water_num()
    print(f"我的水滴数是：{my_water_num}")
    # 获取用户
    while watering_num < 3:
        user_list = get_random_user()
        if user_list:
            # 筛选比我多的
            user_list = get_have_water_for_user(user_list, my_water_num)
            if user_list:
                # 给我浇水
                watering_count = people_get_oneself_water(user_list)
                if watering_count:
                    watering_num += watering_count


if __name__ == '__main__':
    # 卡片签到
    # card_clock()
    # # 卡片分享、
    # card_share()
    # # 水滴签到
    water_clock()
    # # 分享赚水滴，、1天5次
    water_share()
    # 浏览得水滴 1天、两个，各3次
    glance_water()
    # 收自己水滴
    get_oneself_water()
    # 让比我水多的人给我浇水
    author_for_me_water()
