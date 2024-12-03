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


def custom_success_print(message):
    print(f"{'*' * 10}{message}{'*' * 10}")


def custom_fail_print(message):
    print(f"{'='* 10}{message}")


def handler(url, body="", method="get"):
    time.sleep(0.5)
    if method == "post":
        res = requests.post(url, json=body, headers=headers)
    elif method == "put":
        res = requests.put(url, headers=headers)
    else:
        res = requests.get(url, headers=headers)
    return res


def get_handler(parameter_list):
    for parameter in parameter_list:
        url, message = parameter
        res = handler(url)
        res_data = res.json()
        if res_data.get("code") == "200":
            custom_success_print(f"{message}成功")
        else:
            custom_fail_print(f"{message}操作失败:{res_data}")


def post_handler(parameter_list):
    for parameter in parameter_list:
        url, body, message = parameter
        res = handler(url, body, method='post')
        res_data = res.json()
        if res_data.get("errno") == 200:
            return res_data
        else:
            custom_fail_print(f"{message}请求失败:{res_data}")
            return {}


def get_random_user(balance):
    """
    获取用户id列表
    :param balance: 大于指定水滴的用户
    :return:
    """
    parameter_list = [
        (
            'https://e-mall.dfpv.com.cn/web/mp/forest/randomUser',
            {
                "activityId": "402",
                "userId": 7052724
            },
            "获取随机用户"
        )
    ]
    user_id_list = []
    res_data = post_handler(parameter_list)
    data_list = res_data.get('data', [])
    for data in data_list:
        if data['balance'] > balance:
            user_id_list.append(data['userId'])
    return user_id_list


def get_user_water(user_id):
    """
    根据用户id，获取用户没有收的水滴
    :param user_id: 用户id
    :return:
    """
    parameter_list = [
        (
            "https://e-mall.dfpv.com.cn/web/mp/forest/waterIndex",
            {
                "activityId": "402",
                "userId": user_id
            },
            "查询用户可用水滴"
        )
    ]
    water_id_list = []
    res_data = post_handler(parameter_list)
    data_list = res_data.get('data', [])
    for data in data_list:
        water_id_list.append(data['id'])
    return water_id_list


def other_give_me_water(water_id, user_id):
    """
    收别人的水
    :return:
    """
    parameter_list = [
        (
            "https://e-mall.dfpv.com.cn/web/mp/forest/getWater",
            {
            "id": water_id,
            "userId": user_id,
            "operateUserId": "7052724"  # 自己id
            },
            ""
        )
    ]
    res_data = post_handler(parameter_list)
    if res_data:
        custom_success_print(f'{user_id}: 偷取成功，谢谢~~ {res_data.get("errmsg")}')
        return True
    else:
        custom_fail_print(f"{user_id}: 偷取失败，原因：{res_data}")
        return False


def test_get_other_user_water():
    """
    判断用户是否有没有收取的水，有的话尝试给我浇水
    :return:
    """
    user_id_list = get_random_user(0)
    for user_id in user_id_list:
        user_water_id_list = get_user_water(user_id=user_id)
        if user_water_id_list:
            custom_success_print(f"用户:{user_id},有水滴，水滴列表:{user_water_id_list}, 数量:{len(user_water_id_list)}")
            for water_id in user_water_id_list:
                ret = other_give_me_water(water_id, user_id)
                if not ret:
                    break


def execute_get_water():
    water_id_count_list = []
    user_id_list = get_random_user(100)
    if user_id_list:
        print(f"筛选出的用户列表: {user_id_list}")
        for user_id in user_id_list:
            water_id_list = get_user_water(user_id)
            if water_id_list:
                print(f"用户{user_id}: 水滴列表{water_id_list}")
                water_id_count_list.extend(water_id_list)
    return water_id_count_list


def main():
    ret_list = []
    for i in range(5):
        water_id_list = execute_get_water()
        if water_id_list:
            print(f"第{i}轮水滴id列表：{water_id_list}")
            ret_list.extend(water_id_list)
    print(f"----可用水滴列表----:{ret_list}")


if __name__ == '__main__':
    # main()
    for i in range(5):
        print(f'====================={i}======================')
        test_get_other_user_water()
