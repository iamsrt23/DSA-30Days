from collections import deque
class Node:
    def __init__ (self,data):
        self.data = data
        self.right = None
        self.left = None

    
    def reverse_level_order(self,root):
        if root is None:
            return
        queue = deque([root])

        stack = []

        while queue:
            node = queue.popleft()
            stack.append(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        while stack:
            print(stack.pop().data,end =" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)  

root.reverse_level_order(root)