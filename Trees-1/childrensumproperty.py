class Node:
    def __init__ (self,data):
        self.data = data
        self.right = None
        self.left = None

    def childrensum(self,root):
        if root is None or (root.left is None and root.right is None):
            return True
        sum=0
        if root.left:
            sum +=root.left.data
        if root.right:
            sum+=root.right.data

        if root.data == sum:
            return self.childrensum(root.left) and self.childrensum(root.right)
        else:
            return False

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.right = Node(2)

print(root.childrensum(root))