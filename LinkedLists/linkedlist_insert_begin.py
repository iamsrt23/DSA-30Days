class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None 

    def insert(self,data):
        new_node=Node(data)
        new_node.next = self.head
        self.head=new_node


    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next



lst=LinkedList()
lst.insert(12)
lst.insert(8)
lst.insert(10)

lst.display()