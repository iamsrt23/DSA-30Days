# Binary Search Tree

- In the left subtree the value of a node is less than or equal to its parent nodes’value.
- In the right subtree the value of a node is greater than it’s parent node’s value.
- It performs faster than Binary Tree when inserting and deleting Nodes

![Screenshot 2025-01-27 at 4.25.22 PM.png](Binary%20Search%20Tree%2018863324436c80a289fed20206f655d1/Screenshot_2025-01-27_at_4.25.22_PM.png)

**Common Operations on BST:**

- Creation of BST

```python
class BSTNode:
    def __init__(self,data):#time:O(1) and space:O(1)
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBST = BSTNode(None)
```

- Insertion of BST
    - comapre if tree is empty
    - check the value is less than or greater than parent node based on that we insert the value

```python
class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    # Inserting a Value
def insertNode(rootNode,value):#time:O(logN) and space:O(logN)
     # if rootNode is None assign value to rootNode
    if rootNode.data == None:
        rootNode.data = value

    elif value <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild =BSTNode(value)
        else:
            insertNode(rootNode.leftChild,value)

    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(value)
        else:
            insertNode(rootNode.rightChild,value)
                 
    return  "The node has been succesfullly inserted"

        

newBST = BSTNode(None)

print(insertNode(newBST,20))
print(insertNode(newBST,10))
print(newBST.data)
print(newBST.leftChild.data)

```

- Deletion of Node
    - The node to be deleted is a leaf node
    - the node has one child
    - the node has two children
    
    ```python
    class BSTNode:
        def __init__(self,data):
            self.data = data
            self.leftChild = None
            self.rightChild = None
    
        # Inserting a Value
    def insertNode(rootNode,value):#time:O(logN) and space:O(logN)
         # if rootNode is None assign value to rootNode
        if rootNode.data == None:
            rootNode.data = value
    
        elif value <= rootNode.data:
            if rootNode.leftChild is None:
                rootNode.leftChild =BSTNode(value)
            else:
                insertNode(rootNode.leftChild,value)
    
        else:
            if rootNode.rightChild is None:
                rootNode.rightChild = BSTNode(value)
            else:
                insertNode(rootNode.rightChild,value)
                     
        return  "The node has been succesfullly inserted"
        
     # Delete a Node
    # 1. The Node to be deleted is a leaf Node
    # find the leftChild and rightChild Min values
    
    def minValueNode(bstNode):
        while bstNode.leftChild:
            bstNode = bstNode.leftChild
        return bstNode
    
    def delete_node(rootNode,value):#time:O(logN) and space:O(logN)
        if not rootNode:
            return
        
        if value < rootNode.data:
            rootNode.leftChild= delete_node(rootNode.leftChild,value)
        elif value > rootNode.data:
            rootNode.rightChild = delete_node(rootNode.rightChild,value)
        else:
            # Node with no child
            if not rootNode.leftChild and rootNode.rightChild:
                return None
            # Node with only one child
            if not rootNode.leftChild:
                return rootNode.rightChild
            if not rootNode.rightChild:
                return rootNode.leftChild
    
            # Node with two Children
    
            min_node = minValueNode(rootNode.rightChild)
            rootNode.value = min_node.value
            rootNode.rightChild = delete_node(rootNode.rightChild,min_node.value)
        return rootNode
    
    def inOrder(rootNode):
        if not rootNode:
            return
        inOrder(rootNode.leftChild)
        print(rootNode.data)
        inOrder(rootNode.rightChild)
    
    newBST = BSTNode(None)
    
    print(insertNode(newBST,70))
    print(insertNode(newBST,50))
    print(insertNode(newBST,90))
    print(insertNode(newBST,30))
    print(insertNode(newBST,60))
    print(insertNode(newBST,80))
    print(insertNode(newBST,100))
    print(insertNode(newBST,20))
    print(insertNode(newBST,40))
    print(insertNode(newBST,110))
    
    ls = delete_node(newBST,60)
    print("Inorder after deletion:")
    inOrder(ls)
    
    ```
    
- Search for a value

```python
from collections import deque
class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
    # Inserting a Value
def insertNode(rootNode,value):#time:O(logN) and space:O(logN)
     # if rootNode is None assign value to rootNode
    if rootNode.data == None:
        rootNode.data = value

    elif value <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild =BSTNode(value)
        else:
            insertNode(rootNode.leftChild,value)

    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(value)
        else:
            insertNode(rootNode.rightChild,value)
                 
    return  "The node has been succesfullly inserted"
    
    
  # Search node
 
def searchNode(rootNode,value): #time:O(logN) and space:O(logN)
    if rootNode.data == value:
        print("the value is found")
    elif value<rootNode.data:
        if rootNode.leftChild.data == value:
            print("the value is found")
        else:
            searchNode(rootNode.leftChild,value)
    else:
        if rootNode.rightChild.data == value:
            print("the value is found")
        else:
            searchNode(rootNode.rightChild,value)
            
 newBST = BSTNode(None)

print(insertNode(newBST,70))
print(insertNode(newBST,50))
print(insertNode(newBST,90))
print(insertNode(newBST,30))
print(insertNode(newBST,60))
print(insertNode(newBST,80))
print(insertNode(newBST,100))
print(insertNode(newBST,20))
print(insertNode(newBST,40))
print(insertNode(newBST,110))

searchNode(newBST,60)

```

- Traverse all nodes
    - Depth First Search
        - Preorder traversal —>(root,left,right)
        - Inorder traversal—>(root,left,right)
        - Postorder traversal—>(left,right,root)
    - Breadth first search
        - Level Order traversal
        
        ```python
        from collections import deque
        class BSTNode:
            def __init__(self,data):
                self.data = data
                self.leftChild = None
                self.rightChild = None
        
            # Inserting a Value
        def insertNode(rootNode,value):#time:O(logN) and space:O(logN)
             # if rootNode is None assign value to rootNode
            if rootNode.data == None:
                rootNode.data = value
        
            elif value <= rootNode.data:
                if rootNode.leftChild is None:
                    rootNode.leftChild =BSTNode(value)
                else:
                    insertNode(rootNode.leftChild,value)
        
            else:
                if rootNode.rightChild is None:
                    rootNode.rightChild = BSTNode(value)
                else:
                    insertNode(rootNode.rightChild,value)
                         
            return  "The node has been succesfullly inserted"
        
        # Traverse of BST
        # preorder traversal
        def preOrderTraversal(rootNode):#time:O(n) and space:O(n)
        
            if not rootNode:
                return
            print(rootNode.data)
            preOrderTraversal(rootNode.leftChild)
            preOrderTraversal(rootNode.rightChild )
            
        # Inorder traversal
        def inOrderTraversal(rootNode):#time:O(n) and space:O(n)
            if not rootNode:
                return
            inOrderTraversal(rootNode.leftChild)
            print(rootNode.data)
            inOrderTraversal(rootNode.rightChild)
        
        # postorder traversal
        def postOrderTraversal(rootNode):#time:O(n) and space:O(n)
            if not rootNode:
                return
            
            postOrderTraversal(rootNode.leftChild)
            postOrderTraversal(rootNode.rightChild)
            print(rootNode.data)
            
        # levelorder traversal
        def levelOrderTraversal(rootNode): #time:O(n) and space:O(n)
            if not rootNode:
                return
            queue = deque([rootNode])
            result = []
            while queue:
                rootNode = queue.popleft()
                result.append(rootNode.data)
                
                if rootNode.leftChild:
                    queue.append(rootNode.leftChild)
                if rootNode.rightChild:
                    queue.append(rootNode.rightChild)
            return result
        
        newBST = BSTNode(None)
        
        print(insertNode(newBST,70))
        print(insertNode(newBST,50))
        print(insertNode(newBST,90))
        print(insertNode(newBST,30))
        print(insertNode(newBST,60))
        print(insertNode(newBST,80))
        print(insertNode(newBST,100))
        print(insertNode(newBST,20))
        print(insertNode(newBST,40))
        print(insertNode(newBST,110))
        preOrderTraversal(newBST)
        inOrderTraversal(newBST)
        postOrderTraversal(newBST)
        print("----------levelorder------------------")
        print(levelOrderTraversal(newBST))
        ```
        
    
- Deletion of tree

```jsx
class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

  # Inserting a Value
def insertNode(rootNode,value):#time:O(logN) and space:O(logN)
     # if rootNode is None assign value to rootNode
    if rootNode.data == None:
        rootNode.data = value

    elif value <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild =BSTNode(value)
        else:
            insertNode(rootNode.leftChild,value)

    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(value)
        else:
            insertNode(rootNode.rightChild,value)
                 
    return  "The node has been succesfullly inserted"

# delete BST

def delete_BST(rootNode): #time:O(1) and space:O(1)
    rootNode.data = None
    rootNode.lefChild = None
    rootNode.rightChild = None

    return "The BST has been succesfully deleted"       

newBST = BSTNode(None)

print(insertNode(newBST,70))
print(insertNode(newBST,50))
print(insertNode(newBST,90))
print(insertNode(newBST,30))
print(insertNode(newBST,60))
print(insertNode(newBST,80))
print(insertNode(newBST,100))
print(insertNode(newBST,20))
print(insertNode(newBST,40))
print(insertNode(newBST,110))
print("======================")
print(delete_BST(newBST))
```