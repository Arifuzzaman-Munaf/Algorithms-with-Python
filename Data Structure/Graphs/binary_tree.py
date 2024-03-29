class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert_node(data)
                else:
                    self.left = Node(data)
            elif data > self.data:
                if self.right:
                    self.right.insert_node(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)

    def search(self, key):
        if self.data is None:
            return None

        if self.data == key:
            return self

        if self.data < key:
            if self.right:
                return self.right.search(key)
            return None
        else:
            if self.left:
                return self.left.search(key)
            return None


root = Node(27)
root.insert_node(14)
root.insert_node(35)
root.insert_node(10)
root.insert_node(19)
root.insert_node(31)
root.insert_node(42)

print("----------Showing in-order traversal------------")
root.inorder(root)

print("----------Showing pre-order traversal------------")
root.preorder(root)

print("----------Showing post-order traversal------------")
root.postorder(root)

if root.search(10):
    print("Node found")
else:
    print("Node not found")
