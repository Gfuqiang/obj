
"""
# 自定义的类都是type类的实例，下边写法等价
Myclass = type('Myclass', (), {'data': 1})

class Myclass():

    data = 1

my_cls = Myclass()
print(my_cls, Myclass)
print(my_cls.data)

"""

class NotTypeClass():

    def __call__(self, *args, **kwargs):
        print(1)
        return 2



if __name__ == '__main__':
   l = (i for i in range(5))
   print(type(l))
