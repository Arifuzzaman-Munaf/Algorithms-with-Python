class Queue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, value: int):
        self.__queue.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.__queue.pop(0)

    def front(self):
        if self.is_empty():
            return None
        return self.__queue[0]

    def is_empty(self):
        return not self.__queue


queue = Queue()
queue.enqueue(2)
queue.enqueue(20)
queue.enqueue(200)
print(queue.front())

queue.dequeue()
print(queue.front())
print(queue.is_empty())

queue.dequeue()
queue.dequeue()

print(queue.front())
print(queue.is_empty())
