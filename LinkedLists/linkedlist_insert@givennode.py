class Node:
    def __init__(self,data):
        self.data = data
        self.next= None


class LinkedList:
    def __init__ (self):
        self.head=None

    def insert(self,data):
        new_node=Node(data)
        new_node.next = self.head
        self.head=new_node


    def insert_given_node(self,previous_node,new_data):
        if previous_node is None:
            print("Given Node must be Available at Linked List")
            return
        
        new_node=Node(new_data)
        new_node.next = previous_node.next
        previous_node.next=new_node

    def find_node(self,value):
        temp=self.head
        while temp:
            if temp.data == value:
                return temp
            temp = temp.next
        return None

    

    def display(self):
        temp=self.head
        while temp:
            print(str(temp.data)+" ",end=" ")
            temp = temp.next
        print()



lst=LinkedList()
lst.insert(12)
lst.insert(18)
lst.insert(28)
node_with_value =lst.find_node(18)
lst.insert_given_node(node_with_value,20)
lst.display()
