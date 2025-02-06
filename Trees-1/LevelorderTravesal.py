from collections import deque
class Node:
    def __init__ (self,data):
        self.data = data
        self.right = None
        self.left = None

    def levelorder(self,root):
        if root is None:
            return
        
        queue = deque([root])

        while queue:
            current = queue.popleft()
            print(current.data,end=" ")

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)  

root.levelorder(root)
        