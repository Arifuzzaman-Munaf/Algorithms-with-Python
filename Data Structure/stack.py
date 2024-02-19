class Stack:
    def __init__(self):
        self.__storage = []

    def push(self, data):
        self.__storage.append(data)

    def pop(self):
        if self.is_empty():
            return None
        return self.__storage.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.__storage[-1]

    def is_empty(self):
        return (False, True)[not self.__storage]


stack = Stack()
stack.push(2)
stack.push(20)
stack.push(200)
print(stack.top())

stack.pop()
print(stack.top())
print(stack.is_empty())

stack.pop()
stack.pop()

print(stack.top())
print(stack.is_empty())
