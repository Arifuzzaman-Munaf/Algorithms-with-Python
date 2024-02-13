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
        print()

    def get_prev_node(self, position):
        temp = self.head
        count = 1

        while count < position:
            temp = temp.get_next()
            count += 1

        return temp

    def insert_node(self, target_node, position):
        if self.head is None:
            self.head = target_node
            return
        if position == 0:
            target_node.set_next(self.head)
            self.head = target_node

        prev_node = self.get_prev_node(position)
        target_node.set_next(prev_node.get_next())
        prev_node.set_next(target_node)


linked_list = LinkedList()
linked_list.head = Node(5)

second_node = Node(10)
third_node = Node(45)
fourth_node = Node(33)
fifth_node = Node(100)

linked_list.head.set_next(second_node.set_next(third_node.set_next(fourth_node.set_next(fifth_node))))

linked_list.show_list()

new_node = Node(200)
linked_list.insert_node(new_node, 3)
linked_list.show_list()
