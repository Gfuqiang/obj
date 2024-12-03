"""
链表是为了解决动态数量的数据存储
优点:插入，删除不用像数组平移数据
缺点: 查找数据只能遍历，指针占用内存
实现链表
列表中放入的是node节点，节点有val和next两个属性。
添加，删除，是否为空
单项，双向，循环链表的实现
https://blog.csdn.net/Yu_L2/article/details/120399755
"""
import random


class LinkedList:

    def __init__(self, node=None):
        self._head = node
        self.linked = []

    def is_empty(self):
        return self._head is None

    def travel(self):
        """
        遍历节点
        """
        hand = self._head
        while hand is not None:
            print(hand.value)
            hand = hand.next

    def length(self):
        hand = self._head
        count = 0
        while hand is not None:
            count += 1
            hand = hand.next
        return count

    def push(self, val):
        new_node = Node(val)

        if self.is_empty():
            self._head = new_node
        else:
            hand = self._head
            while hand is not None:
                if hand.next is None:
                    hand.next = new_node
                    break
                hand = hand.next


class Node:

    def __init__(self, value):
        self.next = None
        self.value = value


if __name__ == '__main__':
    link_list = LinkedList()
    link_list.push(1)
    link_list.push(1)
    link_list.push(1)
    link_list.travel()


