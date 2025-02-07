from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)  # Dummy node to handle edge cases
        dummy.next = head
        front = back = dummy  # Both pointers start at dummy node
        
        # Move front pointer `n` steps ahead
        for _ in range(n):
            front = front.next
        
        # Move both pointers until front reaches the last node
        while front.next:
            front = front.next
            back = back.next
        
        # Remove the Nth node
        back.next = back.next.next
        
        return dummy.next  # Return the modified list
