# Tree

A tree is a nonlinear data structure with hierarchical relationships between its elements w/o having any cycle, is is basically reversed from real life tree.

Like Drinks Menu 

![Screenshot 2025-01-21 at 5.10.49 PM.png](Tree%2018263324436c801cae8ed99543fe71ef/Screenshot_2025-01-21_at_5.10.49_PM.png)

**Properties:**

- Represent Hierarchical Data
- Each Node has two components: data and a link to its sub category
- Base category and sub categories under it

**Why a Tree:**

- Quicker and Easier access to the data
- Store hierarchical Data, like folder structure , organization structure ,XML/HTML data
- There are many different Types of Data structures which performs better in various situation
    - Binary Search Tree, AVL,Red Black Tree,Trie

![Screenshot 2025-01-21 at 5.16.19 PM.png](Tree%2018263324436c801cae8ed99543fe71ef/Screenshot_2025-01-21_at_5.16.19_PM.png)

**Tree Terminology:**

**Root:** top node without Parent

**Edge:**a link b/w Parent and child

**Leaf:** A node which does not have a children

**Sibling:** children of same Parent

**Ancestor:** Parent, grandParent, great Grand parent of a node

**Depth of node:** a length of the path from root to node

**Height of node:**  a length of the path from the node to the deepest node

**Depth of Tree:** depth of root node

**Height of Tree:** height of root node

**CreateTree.py**

```python
class TreeNode:
    def __init__ (self,data,children):
        self.data = data
        self.children = children

    def __str__(self,level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    

    def addChild(self,TreeNode):
        self.children.append(TreeNode)

tree = TreeNode('Drinks',[])
cold = TreeNode('Cold',[])
hot = TreeNode('Hot',[])
tree.addChild(cold)
tree.addChild(hot)
tea = TreeNode('Tea',[])
coffee = TreeNode('Coffee',[])
cola = TreeNode('Cola',[])
soda = TreeNode('Soda',[])
cold.addChild(cola)
cold.addChild(soda)
hot.addChild(coffee)
hot.addChild(tea)
print(tree)
```

**BinaryTree:**

- Binary trees are the data structures in which each node has at most two children, often referred to as the left and right children.
- Binary tree is a family of data structure (BST, HeapTree, AVL, redblacktrees, Syntax tree)

![Screenshot 2025-01-21 at 5.35.05 PM.png](Tree%2018263324436c801cae8ed99543fe71ef/Screenshot_2025-01-21_at_5.35.05_PM.png)

**Why Binary Tree?**

- Binary tree are a prerequisite for mode advanced trees like BST,AVL, Red Black Trees
- Huffman coding Problem, heap Priority problem and expression parsing problems can be solved efficiently using binary trees

**Types Of Binary Tree:**

- Full Binary Tree

![Screenshot 2025-01-21 at 5.39.18 PM.png](Tree%2018263324436c801cae8ed99543fe71ef/Screenshot_2025-01-21_at_5.39.18_PM.png)

- Perfect Binary Tree

![Screenshot 2025-01-21 at 5.39.52 PM.png](Tree%2018263324436c801cae8ed99543fe71ef/Screenshot_2025-01-21_at_5.39.52_PM.png)

- Complete Binary Tree

![Screenshot 2025-01-21 at 5.40.41 PM.png](Tree%2018263324436c801cae8ed99543fe71ef/Screenshot_2025-01-21_at_5.40.41_PM.png)

- Balanced Binary Tree

![Screenshot 2025-01-21 at 5.41.42 PM.png](Tree%2018263324436c801cae8ed99543fe71ef/Screenshot_2025-01-21_at_5.41.42_PM.png)

Binary Tree Can Be Represented in Two Types

- Linked Lists

![Screenshot 2025-01-21 at 5.43.46 PM.png](Tree%2018263324436c801cae8ed99543fe71ef/Screenshot_2025-01-21_at_5.43.46_PM.png)

- Python Lists (Array)

![Screenshot 2025-01-21 at 5.47.13 PM.png](Tree%2018263324436c801cae8ed99543fe71ef/Screenshot_2025-01-21_at_5.47.13_PM.png)

**Create Binary Tree using Linked List:**

- Creation of Tree
- Insertion of a node
- Deletion of a node
- Search for a value
- Traverse all nodes
- Deletion of tree

```python
class TreeNode:
    def __init__(self,data,):
        self.data = data
        self.leftChild = None
        self.rightChild = None

#  Value of root node
newBT = TreeNode("Drinks")# time:O(1) and space:O(1)
```

**Traversal of Binary Tree:**

**Depth first search:**

- Preorder Traversal
- InOrder traversal
- Post Order Traversal

Breadth first Search:

- Level Order traversal

*Preorder Traversal:*

(Root —> left Subtree —> Right Subtree)  

```python
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.rightChild = None
        self.leftChild = None

newBT = TreeNode("Drinks")
leftChild = TreeNode('Hot')
rightchild = TreeNode('Cold')
newBT.leftChild = leftChild
newBT.rightChild = rightchild

def preorderTraversal(rootNode):# time:O(n)  and Space:O(n)
    if not rootNode: # time:O(1)
        return
    
    print(rootNode.data) # time:O(1)
    preorderTraversal(rootNode.leftChild) # time:O(n/2)
    preorderTraversal(rootNode.rightChild) # time:O(n/2)

preorderTraversal(newBT)
```

*InOrder Traversal:*

(left subtree —> root node —> right sub tree)

```python
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.rightChild = None
        self.leftChild = None

newBT = TreeNode("Drinks")
leftChild = TreeNode('Hot')
rightchild = TreeNode('Cold')
newBT.leftChild = leftChild
newBT.rightChild = rightchild

def inOrderTraversal(rootNode):# time:O(n)  and Space:O(n)
    if not rootNode:# time:O(1)
        return
    
    inOrderTraversal(rootNode.leftChild)# time:O(n/2)
    print(rootNode.data)# time:O(1)
    inOrderTraversal(rootNode.rightChild)# time:O(n/2)

inOrderTraversal(newBT)
```

*PostOrder Traversal:*

(left subtree —> right subtree —> root node)

```python
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.rightChild = None
        self.leftChild = None

newBT = TreeNode("Drinks")
leftChild = TreeNode('Hot')
rightchild = TreeNode('Cold')
tea = TreeNode('tea')
coffee = TreeNode('coffee')
leftChild.leftChild=tea
leftChild.rightChild=coffee

newBT.leftChild = leftChild
newBT.rightChild = rightchild

def postOrderTraversal(rootNode): # time:O(n)  and Space:O(n)
    if not rootNode: #time:O(1)
        return
    
    postOrderTraversal(rootNode.leftChild) # time:O(n/2)
    postOrderTraversal(rootNode.rightChild) # time:O(n/2)
    print(rootNode.data) # time:O(1)

postOrderTraversal(newBT)
```

*LevelOrderTraversal:*

```python
from collections import deque

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.rightChild = None
        self.leftChild = None

newBT = TreeNode("Drinks")
leftChild = TreeNode('Hot')
rightchild = TreeNode('Cold')
tea = TreeNode('tea')
coffee = TreeNode('coffee')
leftChild.leftChild=tea
leftChild.rightChild=coffee

newBT.leftChild = leftChild
newBT.rightChild = rightchild

def levelOrderTraversal(rootNode):
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

print(levelOrderTraversal(newBT)) 
```

**Searching For BinaryTree:**

```python
from collections import deque

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.rightChild = None
        self.leftChild = None

newBT = TreeNode("Drinks")
leftChild = TreeNode('Hot')
rightchild = TreeNode('Cold')
tea = TreeNode('tea')
coffee = TreeNode('coffee')
leftChild.leftChild=tea
leftChild.rightChild=coffee

newBT.leftChild = leftChild
newBT.rightChild = rightchild

def searchBT(rootNode,target):#time:O(n) and space:O(n)
    if not rootNode:
        return False
    
    queue = deque([rootNode])

    while queue:
        rootNode=queue.popleft()
        if rootNode.data  == target:
            return True
        if rootNode.leftChild:
            queue.append(rootNode.leftChild)

        if rootNode.rightChild:
            queue.append(rootNode.rightChild)

    return False
print(searchBT(newBT,"coffee"))
    

         

```

**Insert a node in Binary Tree:**

- A root node is blank
- The tree exists and we have to look for a first vacant place

```python
from collections import deque

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.rightChild = None
        self.leftChild = None

newBT = TreeNode("Drinks")
leftChild = TreeNode('Hot')
rightchild = TreeNode('Cold')
tea = TreeNode('tea')
coffee = TreeNode('coffee')
leftChild.leftChild=tea
leftChild.rightChild=coffee

newBT.leftChild = leftChild
newBT.rightChild = rightchild

def insertNode(rootNode,value):#time:O(n) and space:O(n)
    if not rootNode:
        return TreeNode(value)
    
    queue = deque([rootNode])

    while queue:
        node = queue.popleft()

        if not node.leftChild:
            node.leftChild = TreeNode(value)
            return
        else:
            queue.append(node.leftChild)
        if not node.rightChild:
            node.rightChild = TreeNode(value)
            return
        else:
            queue.append(node.rightChild)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    queue = deque([rootNode])
    result=[]

    while queue:
        node = queue.popleft()
        result.append(node.data)

        if node.leftChild:
            queue.append(node.leftChild)
        if node.rightChild:
            queue.append(node.rightChild)
    return result

    

         

print("Before Insertion:", levelOrderTraversal(newBT))
insertNode(newBT, "Juice")
print("After Insertion:", levelOrderTraversal(newBT))
```

**Delete a node from Binary Tree:**

- Level Order Traversal
- get the deepestNode
- delete the Deepest Node
- delete Node

```python
from collections import deque

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.rightChild = None
        self.leftChild = None

newBT = TreeNode("Drinks")
leftChild = TreeNode('Hot')
rightchild = TreeNode('Cold')
tea = TreeNode('tea')
coffee = TreeNode('coffee')
leftChild.leftChild=tea
leftChild.rightChild=coffee

newBT.leftChild = leftChild
newBT.rightChild = rightchild

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    
    queue = deque([rootNode])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.data)

        if node.leftChild:
            queue.append(node.leftChild)

        if node.rightChild:
            queue.append(node.rightChild)

    return result

def get_the_deepest_Node(rootNode):
    queue = deque([rootNode])

    node = None
    while queue:
        node = queue.popleft()
        if node.leftChild:
            queue.append(node.leftChild)
        if node.rightChild:
            queue.append(node.rightChild)
    return node

def deleteDeepestNode(rootNode,dNode):
    queue = deque([rootNode])
    while queue:
        node = queue.popleft()
        if node is dNode:
            node = None
            return

        if node.rightChild:
            if node.rightChild is dNode:
                node.rightChild = None
                return
            else:
                queue.append(node.rightChild)
        
        if node.leftChild:
            if node.leftChild is dNode:
                node.leftChild = None
                return

            else:
                queue.append(node.leftChild)

def deleteNode(rootNode,target):
    if not rootNode:
        return None
    if rootNode.data == target and not rootNode.leftChild and not rootNode.rightChild:
        return None
    
    queue = deque([rootNode])
    targetNode = None
    
    while queue:
        node = queue.popleft()
        if node.data == target:
            targetNode = node

        if node.leftChild:
            queue.append(node.leftChild)

        if node.rightChild:
            queue.append(node.rightChild)

    
    if targetNode:
        deepstNode = get_the_deepest_Node(rootNode)
        targetNode.data = deepstNode.data
        deleteDeepestNode(rootNode,deepstNode)

    return rootNode

print("Before Deletion:", levelOrderTraversal(newBT))
deleteNode(newBT, "Hot")
print("After Deletion:", levelOrderTraversal(newBT))
```

**Create a BinaryTree Using Python List:**

```python
class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

newBT = BinaryTree(8) #time:O(1) and space:O(n)

```

**Insert a node in BinaryTree:**

- The BinaryTree is Full
- We have to look for a first vacant place

```python
class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self,value): #time:O(1) and space:O(1)
        if self.lastUsedIndex + 1 == self.maxSize:
            return "the Binary tree is Full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex +=1
        return "The value has been successfully inserted"

newBT = BinaryTree(8) #time:O(1) and space:O(n)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))

```

**Searching For a node in Binary Tree(python List)**

```python
class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self,value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "the Binary tree is Full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex +=1
        return "The value has been successfully inserted"
    

    def searchNode(self,nodeValue):
        for i in range(len(self.customList)): #time:O(n) and Space:O(1)
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not FOund"

newBT = BinaryTree(8) #time:O(1) and space:O(n)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.searchNode("Hot"))

```

**PreOrder Traversal of BinaryTree(python list):**

(root>left>right)

```python
class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self,value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "the Binary tree is Full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex +=1
        return "The value has been successfully inserted"
    

    # def searchNode(self,nodeValue):
    #     for i in range(len(self.customList)): #time:O(n) and Space:O(1)
    #         if self.customList[i] == nodeValue:
    #             return "Success"
    #     return "Not FOund"
    
    def preOrderTraversal(self,index):#time:O(n) and Space:O(n)
        if index > self.lastUsedIndex:
            return
        
        print(self.customList[index])
        self.preOrderTraversal(index*2) #
        self.preOrderTraversal(index*2 +1)
    

newBT = BinaryTree(8) #time:O(1) and space:O(n)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
# print(newBT.searchNode("Hot"))
newBT.preOrderTraversal(1)

```

**InOrder traversal:**

(left>root>right)

```python
class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self,value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "the Binary tree is Full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex +=1
        return "The value has been successfully inserted"
    

    def inOrderTraversal(self,index):#time:O(n) and Space:O(n)
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)
    

newBT = BinaryTree(8) #time:O(1) and space:O(n)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
newBT.inOrderTraversal(1)

```

**PostOrder Traversal:**

(left>right>root)

```python
class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self,value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "the Binary tree is Full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex +=1
        return "The value has been successfully inserted"
    

    def postOrderTraversal(self,index):#time:O(n) and Space:O(n)

        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2+1)
        print(self.customList[index])
        
    

newBT = BinaryTree(8) #time:O(1) and space:O(n)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
newBT.postOrderTraversal(1)

```

**Level Order Traversal:**

(level1 > level2 > level3)

```python
class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self,value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "the Binary tree is Full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex +=1
        return "The value has been successfully inserted"
    

    def levelOrderTraversal(self,index):#time:O(n) and Space:O(1)

        for i in range(index,self.lastUsedIndex+1):
            print(self.customList[i])
        
    

newBT = BinaryTree(8) #time:O(1) and space:O(n)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
newBT.levelOrderTraversal(1)

```

**Delete a Node from BT:**

- Level Order Traversal
- Deepest Node = lastUsedIndex

```python
class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self,value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "the Binary tree is Full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex +=1
        return "The value has been successfully inserted"
    

    def levelOrderTraversal(self,index):
        for i in range(index,self.lastUsedIndex+1):
            print(self.customList[i])
        
    
    def deleteNode(self,value):#time:O(n) and Space:O(n)
        if self.lastUsedIndex == 0:
            return "There is Node to delete"
        
        for i in range(1,self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -=1
                return "The Node Has been suceessfully deleted"

        

newBT = BinaryTree(8) #time:O(1) and space:O(n)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.deleteNode("Hot"))
newBT.levelOrderTraversal(1)

```

**Delete Entire BinaryTree:**

- customList = None

```python
class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self,value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "the Binary tree is Full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex +=1
        return "The value has been successfully inserted"
    

    def levelOrderTraversal(self,index):
        for i in range(index,self.lastUsedIndex+1):
            print(self.customList[i])
        
    
    def deleteBT(self):#time:O(1) and space:O(1)
        self.customList = None
        return "The BT has been successfully deleted"

        

newBT = BinaryTree(8) #time:O(1) and space:O(n)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.deleteBT())
newBT.levelOrderTraversal(1)

 
```

![Screenshot 2025-01-22 at 4.40.03 PM.png](Tree%2018263324436c801cae8ed99543fe71ef/Screenshot_2025-01-22_at_4.40.03_PM.png)