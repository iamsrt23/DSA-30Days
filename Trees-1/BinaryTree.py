class Node:
    def __init__ (self,data):
        self.data = data
        self.right = None
        self.left = None



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)  