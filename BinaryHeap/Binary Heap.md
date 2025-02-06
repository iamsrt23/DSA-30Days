# Binary Heap

A Binary Heap is a Binary Tree with following properties

- A Binary Geap us either Min Heap or Max Heap. In a Min Binary Heap, they key at root must be minimum among all keys present in Binary Heap. The same Property must be recursively true for all nodes in Binary Tree.
- It’s a complete tree (All levels are completely filled except possibly the last level and the last level has all keys as left as possible). This property of Binary tree Heap makes them suitable to be stored in an array.

![Screenshot 2025-01-27 at 7.30.26 PM.png](Binary%20Heap%2018863324436c80b99f41de81eb18f725/Screenshot_2025-01-27_at_7.30.26_PM.png)

Why we need a Binary Heap?

Find the min or max number among a set of numbers in logN time. And also we want to make sure that inserting additional numbers does not take more than O(logN) time.

**possible solutions:**

- store the numbers in sorted Array
- store the numbers in Linked List in sorted manner

**practical use:**

- Prim’s Algorithm
- Heap Sort
- Priority Queue

Types Of Binaryheap:

- Min heap - The value of each node is lessthan or equal to the value of both its children.

![Screenshot 2025-01-27 at 7.30.26 PM.png](Binary%20Heap%2018863324436c80b99f41de81eb18f725/Screenshot_2025-01-27_at_7.30.26_PM%201.png)

- Max heap - it is exactly the opposite of min heap that is the value of each node is more than or equal to the value of both its children.

![Screenshot 2025-01-27 at 7.38.13 PM.png](Binary%20Heap%2018863324436c80b99f41de81eb18f725/Screenshot_2025-01-27_at_7.38.13_PM.png)

**Common Operations on Binary Heap:**

- creation of Binary Heap
    - initialize fixed size list
    - set size of Binary Heap to 0
    
    ```python
    # Creating Binary Heap
    
    class Heap:
        def __init__(self,size): #time:O(1) and space:O(N){based on size}
            self.customList = (size+1) *[None]
            self.heapSize = 0
            self.maxSize = size+1
    
    newBinaryHeap = Heap(5)
    ```
    
- Peek top of Binary Heap

![Screenshot 2025-01-27 at 7.48.37 PM.png](Binary%20Heap%2018863324436c80b99f41de81eb18f725/Screenshot_2025-01-27_at_7.48.37_PM.png)

```python
# Creating Binary Heap

class Heap:
    def __init__(self,size): #time:O(1) and space:O(N){based on size}
        self.customList = (size+1) *[None]
        self.heapSize = 0
        self.maxSize = size+1

# Peek
def peek(rootNode): #time:O(1) and space:O(1)
    if not rootNode:
        return
    else:
        return rootNode.customList[1]
    

newBinaryHeap = Heap(5)
```

- Size of Binary Heap

![Screenshot 2025-01-27 at 7.51.12 PM.png](Binary%20Heap%2018863324436c80b99f41de81eb18f725/Screenshot_2025-01-27_at_7.51.12_PM.png)

```python
# Creating Binary Heap

class Heap:
    def __init__(self,size): #time:O(1) and space:O(N){based on size}
        self.customList = (size+1) *[None]
        self.heapSize = 0
        self.maxSize = size+1

# Peek
def peek(rootNode): #time:O(1) and space:O(1)
    if not rootNode:
        return
    else:
        return rootNode.customList[1]
    
# size
def sizeofHeap(rootNode):#time:O(1) and space:O(1)
    if not rootNode:
        return
    else:
        return rootNode.heapSize
newBinaryHeap = Heap(5)
print(sizeofHeap(newBinaryHeap))
```

- Exttract Min/ Extract Max

```python
# Creating Binary Heap

class Heap:
    def __init__(self,size): #time:O(1) and space:O(N){based on size}
        self.customList = (size+1) *[None]
        self.heapSize = 0
        self.maxSize = size+1

# Peek
def peek(rootNode): #time:O(1) and space:O(1)
    if not rootNode:
        return
    else:
        return rootNode.customList[1]
    
# size
def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

# level Order

def levelorder(rootNode): #time:O(n) and space:O(1)
    if not rootNode:
        return
    for i in range(1,rootNode.heapSize+1):
        print(rootNode.customList[i])

# Insertion a Node
# Heapify Method

def heapifyTreeInsert(rootNode,index,heapType):#time:O(logN) and space:O(logN)
    parentIndex = int(index//2)
    if index<=1:
        return
    if heapType=="Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            # swap the nodes
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode,parentIndex,heapType)
    elif heapType=="Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            # swap the nodes
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode,parentIndex,heapType)

def insertNode(rootNode,value,heapType):#time:O(logN) and space:O(logN)
    # Check the size of heap full or not
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary is Full"
    rootNode.customList[rootNode.heapSize + 1] = value
    rootNode.heapSize +=1
    heapifyTreeInsert(rootNode,rootNode.heapSize,heapType)
    return "The value has been successfully inserted"

# Extract Method

def heapifyTreeExtract(rootNode,index,heapType):#time:O(logN) and space:O(logN)
    leftIndex = index *2 
    rightIndex = index*2+1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex]=temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex]=temp
            return
    else:
        if heapType == "Min":
            if rootNode.customList[index] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild]=temp
        else:
            if rootNode.customList[index] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild]=temp
        heapifyTreeExtract(rootNode,swapChild,heapType)

def extractNode(rootNode,heapType):#time:O(logN) and space:O(logN)
    if rootNode.heapSize ==0:
        return
    else:
        extractNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -=1
        heapifyTreeExtract(rootNode,1,heapType)
        return extractNode

        
                

 

newBinaryHeap = Heap(5)
insertNode(newBinaryHeap,4,"Max")
insertNode(newBinaryHeap,6,"Max")
insertNode(newBinaryHeap,2,"Max")
insertNode(newBinaryHeap,8,"Max")
print(extractNode(newBinaryHeap,"Max"))
levelorder(newBinaryHeap)
print(sizeofHeap(newBinaryHeap))

```

- Traversal of Binary Heap
    - preorder
    - inorder
    - postorder
    - levelorder
    
    ![Screenshot 2025-01-27 at 7.53.59 PM.png](Binary%20Heap%2018863324436c80b99f41de81eb18f725/Screenshot_2025-01-27_at_7.53.59_PM.png)
    

```python
# Creating Binary Heap

class Heap:
    def __init__(self,size): #time:O(1) and space:O(N){based on size}
        self.customList = (size+1) *[None]
        self.heapSize = 0
        self.maxSize = size+1

# Peek
def peek(rootNode): #time:O(1) and space:O(1)
    if not rootNode:
        return
    else:
        return rootNode.customList[1]
    
# size
def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

# level Order

def levelorder(rootNode): #time:O(n) and space:O(1)
    if not rootNode:
        return
    for i in range(1,rootNode.heapSize+1):
        print(rootNode.customList[i])

newBinaryHeap = Heap(5)
print(sizeofHeap(newBinaryHeap))

```

- Insert value in Binary Heap
    - Check the value with root node if it is minheap swap the node with it’s parent value

```python
# Creating Binary Heap

class Heap:
    def __init__(self,size): #time:O(1) and space:O(N){based on size}
        self.customList = (size+1) *[None]
        self.heapSize = 0
        self.maxSize = size+1
# size
def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize
# level Order

def levelorder(rootNode): #time:O(n) and space:O(1)
    if not rootNode:
        return
    for i in range(1,rootNode.heapSize+1):
        print(rootNode.customList[i])

# Insertion a Node
# Heapify Method

def heapifyTreeInsert(rootNode,index,heapType):#time:O(logN) and space:O(logN)
    parentIndex = int(index//2)
    if index<=1:
        return
    if heapType=="Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            # swap the nodes
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode,parentIndex,heapType)
    elif heapType=="Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            # swap the nodes
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode,parentIndex,heapType)

def insertNode(rootNode,value,heapType):#time:O(logN) and space:O(logN)
    # Check the size of heap full or not
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary is Full"
    rootNode.customList[rootNode.heapSize + 1] = value
    rootNode.heapSize +=1
    heapifyTreeInsert(rootNode,rootNode.heapSize,heapType)
    return "The value has been successfully inserted"

 

newBinaryHeap = Heap(5)
insertNode(newBinaryHeap,4,"Max")
insertNode(newBinaryHeap,6,"Max")
insertNode(newBinaryHeap,2,"Max")
insertNode(newBinaryHeap,8,"Max")
levelorder(newBinaryHeap)
print(sizeofHeap(newBinaryHeap))
```

- Delete the entire Binary Heap

```python
# Creating Binary Heap

class Heap:
    def __init__(self,size): #time:O(1) and space:O(N){based on size}
        self.customList = (size+1) *[None]
        self.heapSize = 0
        self.maxSize = size+1

# Peek
def peek(rootNode): #time:O(1) and space:O(1)
    if not rootNode:
        return
    else:
        return rootNode.customList[1]
    
# size
def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

# level Order

def levelorder(rootNode): #time:O(n) and space:O(1)
    if not rootNode:
        return
    for i in range(1,rootNode.heapSize+1):
        print(rootNode.customList[i])

# Insertion a Node
# Heapify Method

def heapifyTreeInsert(rootNode,index,heapType):#time:O(logN) and space:O(logN)
    parentIndex = int(index//2)
    if index<=1:
        return
    if heapType=="Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            # swap the nodes
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode,parentIndex,heapType)
    elif heapType=="Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            # swap the nodes
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode,parentIndex,heapType)

def insertNode(rootNode,value,heapType):#time:O(logN) and space:O(logN)
    # Check the size of heap full or not
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary is Full"
    rootNode.customList[rootNode.heapSize + 1] = value
    rootNode.heapSize +=1
    heapifyTreeInsert(rootNode,rootNode.heapSize,heapType)
    return "The value has been successfully inserted"

# Extract Method

def heapifyTreeExtract(rootNode,index,heapType):#time:O(logN) and space:O(logN)
    leftIndex = index *2 
    rightIndex = index*2+1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex]=temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex]=temp
            return
    else:
        if heapType == "Min":
            if rootNode.customList[index] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild]=temp
        else:
            if rootNode.customList[index] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild]=temp
        heapifyTreeExtract(rootNode,swapChild,heapType)

def extractNode(rootNode,heapType):#time:O(logN) and space:O(logN)
    if rootNode.heapSize ==0:
        return
    else:
        extractNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -=1
        heapifyTreeExtract(rootNode,1,heapType)
        return extractNode

        
# Delete Binary Heap

def deleteBinaryHeap(rootNode):#time:O(1) and space:O(1)
    rootNode.customList = None

 

newBinaryHeap = Heap(5)
insertNode(newBinaryHeap,4,"Max")
insertNode(newBinaryHeap,6,"Max")
insertNode(newBinaryHeap,2,"Max")
insertNode(newBinaryHeap,8,"Max")
deleteBinaryHeap(newBinaryHeap)
print(extractNode(newBinaryHeap,"Max"))
levelorder(newBinaryHeap)
print(sizeofHeap(newBinaryHeap))

```

**Implementation options:**

- Array Implementations ✅
- Reference / pointer Implementation

![Screenshot 2025-01-27 at 7.41.42 PM.png](Binary%20Heap%2018863324436c80b99f41de81eb18f725/Screenshot_2025-01-27_at_7.41.42_PM.png)

![Screenshot 2025-01-28 at 11.48.30 AM.png](Binary%20Heap%2018863324436c80b99f41de81eb18f725/Screenshot_2025-01-28_at_11.48.30_AM.png)