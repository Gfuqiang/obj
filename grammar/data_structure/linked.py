"""
链表是为了解决动态数量的数据存储
优点:插入，删除不用像数组平移数据
缺点: 查找数据只能遍历，指针占用内存
实现链表
列表中放入的是node节点，节点有val和next两个属性。
添加，删除，是否为空
"""
import random


class Linked:

    def __init__(self):
        self.linked = []

    def push(self, val):
        node = Node(val)
        if len(self.linked) == 0:
            self.linked.append(node)
        else:
            index = len(self.linked) - 1
            before_node = self.linked[index]
            before_node.next = node
            self.linked.append(node)

    def pop(self, val):
        for node in self.linked:
            if node.value == val:
                if node.next is None:
                    self.linked.remove(node)
                    return
                after_node = node.next
                for before_node in self.linked:
                    if before_node == node:
                        before_node.next = after_node
                self.linked.remove(node)

    def get_linked(self):
        return self.linked


class Node:

    def __init__(self, value):
        self.next = None
        self.value = value


if __name__ == '__main__':
    linked = Linked()
    list_data = [i for i in range(10)]
    random.shuffle(list_data)
    for i in list_data:
        linked.push(i)
    linked.pop(9)
    linked_data = linked.get_linked()
    for data in linked_data:
        print(f"val: {data.value}  next: {data.next}")


