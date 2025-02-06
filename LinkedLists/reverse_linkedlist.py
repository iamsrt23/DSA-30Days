class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__ (self):
        self.head = None
    
    def insert_at_end(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head=new_node
            return

        temp = self.head

        while temp.next:
            temp =temp.next

        temp.next = new_node

    def reverse(self):
        prev=None
        temp = self.head

        while temp:
            new_node = temp.next

            '''We have to do like these take 3 nodes 
            node1(prev)--> node2(temp)-->node3(front)
            we have to assign
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
            it will change like this
            node1(prev)<-- node2(temp)<--node3(front)
            '''

            temp.next = prev
            prev = temp
            temp = new_node
        self.head = prev


    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        
    



lst = LinkedList()
lst.insert_at_end(20)
lst.insert_at_end(10)
lst.insert_at_end(30)
lst.display()
print()
print("reverseLinked List")
lst.reverse()

lst.display()