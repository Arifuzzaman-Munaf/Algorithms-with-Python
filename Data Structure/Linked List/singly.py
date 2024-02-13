class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_next(self, node):
        self.__next = node
        return self

    def get_next(self):
        return self.__next


class LinkedList:
    def __init__(self):
        self.head = None

    def show_list(self):
        temp = self.head
        while temp:
            print(temp.get_value(), end=" ")
            temp = temp.get_next()


linked_list = LinkedList()
linked_list.head = Node(5)

second_node = Node(10)
third_node = Node(45)
fourth_node = Node(33)
fifth_node = Node(100)

linked_list.head.set_next(second_node.set_next(third_node.set_next(fourth_node.set_next(fifth_node))))

linked_list.show_list()
