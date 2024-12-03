"""
状态模式
旨在将判断逻辑维护的状态，转换为简单的方式控制状态
transitions 官方文档:
https://github.com/pytransitions/transitions?tab=readme-ov-file#diagrams
"""
from enum import Enum

import faker
from faker import Faker
from faker.providers import DynamicProvider
from transitions import Machine




class UserStatus(Enum):
    NEW_CREATE = 'new_create'  # 新建
    NORMAL = 'normal'  # 正常
    REST_PWD = 'rest_pwd'  # 密码已重置
    INVALID = 'invalid'  # 密码失效
    EXPIRE = 'expire'  # 已过期


class Request:

    pass


class UserStatusMachine:

    status = [status.value for status in UserStatus]

    def __init__(self, user, initial_status, model=None):
        self.user = user

        if not model:
            model = self

        transitions = [
            {'trigger': 'rest_pwd', 'source': '*', 'dest': 'rest_pwd'},
        ]

        # 定义状态机，需要定义初始状态
        self.machine = Machine(
            model=model, states=UserStatusMachine.status, initial=initial_status, transitions=transitions)
        # 添加状态转换
        self.machine.add_transition(trigger='recover', source=UserStatus.EXPIRE.value, dest=UserStatus.NORMAL.value)

def faker_test():
    fake = Faker()
    for _ in range(5):
        file_name = fake.file_name(category='office', extension=[])
        print(file_name)
        print(fake.file_path(depth=3, extension=[]) + '/' + file_name)

def custom_provider():
    fake = Faker()

    my_word_list = [
        'danish', 'cheesecake', 'sugar',
        'Lollipop', 'wafer', 'Gummies',
        'sesame', 'Jelly', 'beans',
        'pie', 'bar', 'Ice', 'oat']

    print(fake.sentence())
    # 'Expedita at beatae voluptatibus nulla omnis.'

    print(fake.sentence(ext_word_list=my_word_list))

def dynamic_provider():
    medical_professions_provider = DynamicProvider(
        provider_name="medical_profession",
        elements=[("nginx", 1), {"docker": 1}, "tomcat", "systemctl", "systemctl-journal"],
    )

    fake = Faker()

    # then add new provider to faker instance
    fake.add_provider(medical_professions_provider)

    # now you can use:
    print(fake.medical_profession())

from faker import factory
from dataclasses import dataclass

@dataclass
class Book:

    title: str
    author_name: str

def user_info_provider():
    fake = faker.Faker('zh_CN')
    print(fake.name())
    print(fake.phone_number())


if __name__ == '__main__':
    # req = Request()
    # user_status = UserStatusMachine('wang', UserStatus.EXPIRE.value, model=req)
    # print(req.state)
    # # 触发状态转换
    # req.recover()
    # print(req.state)
    # req.trigger('rest_pwd')
    # print(req.state)

    # faker_test()
    # custom_provider()
    # dynamic_provider()
    user_info_provider()

