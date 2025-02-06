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

def inOrderTraversal(rootNode):#time:O(n) and space:O(n)
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):#time:O(n) and space:O(n)
    if not rootNode:
        return
    
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

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
# Search Node
def searchNode(rootNode,value):
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


# Delete a Node
# 1. The Node to be deleted is a leaf Node

def minValueNode(bstNode):
    while bstNode.leftChild:
        bstNode = bstNode.left
    return bstNode

def delete_node(rootNode,value):
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



# delete BST

def delete_BST(rootNode):
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
preOrderTraversal(newBST)
inOrderTraversal(newBST)
postOrderTraversal(newBST)
print("----------levelorder------------------")
print(levelOrderTraversal(newBST))
searchNode(newBST,60)
print("======================")
ls = delete_node(newBST,60)
print("Inorder after deletion:")
inOrder(ls)
print("======================")
print(delete_BST(newBST))