class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Creating the linked list using provided array
    def create_list(self, arr):
        # when arr in empty return a None list
        if not arr:
            return None

        # creating the head node
        # assigning the head reference to current_node
        current_node = self.head = Node(arr[0])

        for i in arr[1:]:
            new_node = Node(i)
            current_node.next = new_node
            new_node.prev = current_node
            current_node = current_node.next
        return self.head

    # this function will show the list in structured way
    def show_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" ")
            current_node = current_node.next
        print()

    # get the previous node of current node
    def get_prev_node(self, position):
        current_node = self.head
        count = 0

        while count < position - 1:
            current_node = current_node.next
            count += 1

        return current_node

    def insert_node(self, value, position):
        # checking if list is empty or nor
        if not self.head and position > 0:
            return -1

        target_node = Node(value)
        # if the target node has to be added head then
        # just make the head as next node of target node
        # make the target node as head
        if position == 0:
            target_node.next = self.head
            self.head.prev = target_node
            self.head = target_node
            return

        # get the previous node of position
        prev_node = self.get_prev_node(position)

        # check if prev_node of the list or not
        if prev_node.next:
            prev_node.next.prev = target_node
        target_node.next = prev_node.next
        prev_node.next = target_node
        target_node.prev = prev_node

    def delete_node_by_position(self, position):
        # if list is empty then return
        if self.head is None:
            return

        # if the position denotes head node
        # then remove the node
        # make the next node as head or set none for single element list
        if position == 0:
            self.head = self.head.next
            return

        # get the prev node
        prev_node = self.get_prev_node(position)
        target_node = prev_node.next  # node to delete

        # link the prev node with the next node of target node
        if target_node.next:
            target_node.next.prev = prev_node
        prev_node.next = target_node.next


list_array = [10, 20, 30, 40, 50, 60]
linked_list = LinkedList()
linked_list.create_list(list_array)
linked_list.show_list()

linked_list.insert_node(100, 0)
linked_list.show_list()

linked_list.delete_node_by_position(7)
linked_list.show_list()
