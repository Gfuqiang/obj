

def demo1():
    import aiocron, asyncio
    @aiocron.crontab('*/1 * * * *')
    async def attime():
        print('run')

    asyncio.get_event_loop().run_forever()


class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    def __getattribute__(self, item):
        print(f'__getattribute__ execute')

    x = property(getx, setx, delx, "I'm the 'x' property.")


class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage


if __name__ == '__main__':
    # d1 = Demo()
    # d1.test_cls_decorator(11111)
    # demo1()
    c = C()
    c._x = 1
    print(c._x)
    # print(c.x)
    # p = Parrot()
    # print(p.voltage)
