from heapq import heappush, heappop
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class HeapNode:
    def __init__(self,node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for l in lists:
            if l:
                heappush(min_heap,HeapNode(l))
        
        dummy = ListNode()
        merge = dummy

        while min_heap:
            heap_node = heappop(min_heap)
            merge.next = heap_node.node
            merge = merge.next

            if heap_node.node.next:
                heappush(min_heap,HeapNode(heap_node.node.next))
        return dummy.next
        