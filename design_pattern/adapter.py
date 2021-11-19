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
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


if __name__ == '__main__':
    objects = [Computer('big c')]
    human = Human('alek')
    objects.append(Adapter(human, dict(play=human.speak)))
    apple = Apple('red')
    objects.append(Adapter(apple, dict(play=apple.descrip)))

    for i in objects:
        print(i.__dict__)
        print(f"obj: {i}, {i.play()}\n")

