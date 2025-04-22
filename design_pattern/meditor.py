"""
中介模式
"""
class Houselnfo:

    # "房源信息"!
    def __init__(self, address, area, price, has_window, bathroom, kitchen, owner):
        self.area = area
        self.__price = price
        self. _hasWindow = has_window
        self._hasBathroom = bathroom
        self.__haskitchen = kitchen
        self._address = address
        self._owner = owner

    def getAddress(self):
        ...

class HousingAgency:
    """房屋中介"""
    def __init__(self, name):
        self.__name = name
        self.__house_infos = []

    def get_name(self):
        return self.__name

    def add_house_info(self, house_info):
        self.__house_infos.append(house_info)

    def remove_house_info(self, house_info):
        for info in self.__house_infos:
            if info == house_info:
                self.__house_infos.remove(info)

    def get_search_condition(self, description):
        return description



class HouseOwner:

    def __init__(self, name):
        self.__name = name
        self.__house_info = None

    def get_name(self):
        return self.__name

    def publish_house_info(self, agency):
        agency.add_house_info(self.__house_info)
        self.__house_info.show_info()

    def set_house_info(self, address, area, price, has_window, bathroom, kitchen):
        self.__house_info = Houselnfo(address, area, price, has_window, bathroom, kitchen, self)

class Customer:
    ...


if __name__ == '__main__':
    my_house = HousingAgency('我爱我家')
    zhangsan = HouseOwner("张三")
    zhangsan.set_house_info('上地西里', '上地', 2500, 1, 1, 1)
    zhangsan.publish_house_info(my_house)
