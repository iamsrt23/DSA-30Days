class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__ (self):
        self.head=None


    def insert_at_end(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def cycle_start(self):
        slow,fast = self.head,self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = self.head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow
        return None