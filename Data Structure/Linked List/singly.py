class Node:

    # initialized the node
    # encapsulated the variables
    # initialized getter and setter
    def __init__(self, value):
        self.__value = value
        self.__next = None

    # set value of node
    def set_value(self, value):
        self.__value = value

    # get the value of node
    def get_value(self):
        return self.__value

    # link  next node
    def set_next(self, node):
        self.__next = node
        return self

    # get next node
    def get_next(self):
        return self.__next


class LinkedList:
    def __init__(self):
        self.head = None

    # this function will show the list in structured way
    def show_list(self):
        temp = self.head
        while temp:
            print(temp.get_value(), end=" ")
            temp = temp.get_next()
        print()

    # get the previous node of current node
    def get_prev_node(self, position):
        temp = self.head
        count = 1

        while count < position:
            temp = temp.get_next()
            count += 1

        return temp

    def insert_node(self, target_node, position):

        # if list is empty then add the target node as head
        if self.head is None:
            self.head = target_node
            return

        # if the target node has to be added as then
        # just make the head as next node of target node
        # make the target node as head
        if position == 0:
            target_node.set_next(self.head)
            self.head = target_node

        # get previous node and link that node to target node
        # the target node will link the next node of prev node
        prev_node = self.get_prev_node(position)
        target_node.set_next(prev_node.get_next())
        prev_node.set_next(target_node)

    def delete_node_by_position(self, position):
        # if list is empty then return
        if self.head is None:
            return
        # get the prev node
        # link the prev node with the next node of target node
        prev_node = self.get_prev_node(position)
        target_node = prev_node.get_next()
        prev_node.set_next(target_node.get_next())

    def delete_node_by_value(self, value):
        temp = self.head

        # if list is empty then return
        if temp is None:
            return

        # if the value is found in head node
        # then remove the node
        # make the next node as head or set none for single element list
        if temp.get_value() == value:
            self.head = temp.get_next()
            temp = None
            return

        # get the prev of node target node
        while temp.get_next() and temp.get_next().get_value() != value:
            temp = temp.get_next()

        # get the target node
        # link the prev node with the next node of target node
        if temp.get_next():
            target_node = temp.get_next()
            temp.set_next(target_node.get_next())
            target_node.set_next(None)
        else:
            print(f"Node with value {value} not found in the linked list.")


linked_list = LinkedList()
linked_list.head = Node(5)

second_node = Node(10)
third_node = Node(45)
fourth_node = Node(33)
fifth_node = Node(100)

# created a linked list of 5 elements
linked_list.head.set_next(second_node.set_next(third_node.set_next(fourth_node.set_next(fifth_node))))

linked_list.show_list()

new_node = Node(200)
linked_list.insert_node(new_node, 3)
linked_list.show_list()

linked_list.delete_node_by_position(3)
linked_list.show_list()

new_node = Node(500)
linked_list.insert_node(new_node, 4)
linked_list.show_list()

linked_list.delete_node_by_value(5)
linked_list.show_list()
