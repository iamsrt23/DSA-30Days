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
