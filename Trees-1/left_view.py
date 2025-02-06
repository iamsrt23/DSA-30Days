from collections import deque
class Node:
    def __init__ (self,data):
        self.data = data
        self.right = None
        self.left = None
    
    def left_data(self,root):
        if root is None:
            return []
        queue=deque([root])
        res=[]
        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()
                if i == 0:
                    res.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)

print(root.left_data(root))
