"""
建造者模式：
    实现思路：提供指挥者类和建造者类，建造者可以生产属性值不同的产品。
    场景：需要创建一个复杂的对象（对象由多个部分构成，且要经过多个步骤，且步骤还要遵循一定顺序）
            要求一个对象要有多种表现，并希望对象的构建与表现解耦。
            想要在某个时间点创建，在稍后的时间里进行访问。
    与工厂模式区别：
        工厂模式在代码启动后就创建好了对象，一个factory生产指定对象。
"""

"""
举例：
    工厂模式生产指定配置的电脑
    建造者模式可以生产任意自由配置的电脑
"""


class Computer:

    def __init__(self, serial_number):
        self.serial = serial_number
        self.cpu = None
        self.memory = None
        self.network = None

    def __str__(self):
        return f'Computer conf is cpu: {self.cpu}、 memory: {self.memory}、 network: {self.network}'


class ComputerBuild:
    """
    建造者
    提供建造方法
    """

    def __init__(self):
        self.comp = Computer('A1-001')

    # 以下将每个部件安装功能解耦
    def configure_cpu(self, cpu):
        self.comp.cpu = cpu

    def configure_memory(self, memory):
        self.comp.memory = memory

    def configure_network(self, network):
        self.comp.network = network


class HardwareEngineer:
    """
    指挥者
    提供需要建造内容的参数
    """
    def __init__(self):
        self.builder = None

    def build_computer(self, cpu, memory, network):
        self.builder = ComputerBuild()
        _ = [
            step for step in (
            self.builder.configure_cpu(cpu),
            self.builder.configure_memory(memory),
            self.builder.configure_network(network)
            )
        ]

    @property
    def computer(self):
        return self.builder.comp


if __name__ == '__main__':
    hardware_engineer = HardwareEngineer()
    hardware_engineer.build_computer('i7', '16G', 'a3002')
    print(hardware_engineer.computer)
    hardware_engineer.build_computer('i9', '32G', 'a3333')
    print(hardware_engineer.computer)


