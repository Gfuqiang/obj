class Node():

    def __init__(self, element=None, next_node=None):
        self.element = element
        self.next_node = next_node


class LinkedList():

    def __init__(self, size=0):
        self.size = size
        self.first_node = Node()

    def size(self):
        return self.size

    def is_empty(self):
        if self.size:
            return True
        return False

    def clear(self):
        self.size = 0
        self.first_node = None

    def get(self, index):
        return self.node(index).element

    def set(self):
        pass

    def add(self, index, element):
        if index == 0:
            self.first_node = Node(element, None)
        node: Node = self.node(index - 1)
        node.next_node = Node(element, node.next_node)
        self.size += 1

    def node(self, index):
        node = self.first_node
        for i in range(index):
            node = node.next_node
        return node


if __name__ == '__main__':
    link_list = LinkedList()
    link_list.add(0, 1)
    result = link_list.get(0)
    print(result)
