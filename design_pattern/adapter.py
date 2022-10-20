"""
适配器模式
Human，Apple 两个类没有play 方法，将他们注册进入适配器类Adapter中，都拥有了play方法可以和computer类的play一样统一调用。
相当于给Human，Apple两个类适配了paly方法。
"""


class Human:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} the human"

    def speak(self):
        return "say hello"


class Apple:

    def __init__(self, color):
        self.color = color
        self.name = "apple"

    def descrip(self):
        return f'apple is {self.color}'


class Computer:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"computer-{self.name}"

    def play(self):
        return "play game"


class Adapter:

    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.name = 'adapter'
        # TODO
        # 给obj适配属性
        self.__dict__.update(adapted_methods)

    def __str__(self):
        # TODO
        # 将适配器类返回为注册类，实例化的是注册类，而不是Adapter类
        return str(self.obj)


if __name__ == '__main__':
    objects = [Computer('big c')]
    human = Human('alek')
    # 注册human类到适配器中
    objects.append(Adapter(human, dict(play=human.speak, name=human.name)))
    apple = Apple('red')
    objects.append(Adapter(apple, dict(play=apple.descrip, name=apple.name)))

    for i in objects:
        print(i.__dict__)
        print(i.name)
        print(f"obj: {i}, {i.play()}\n")

