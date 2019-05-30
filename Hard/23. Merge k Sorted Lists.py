# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        headNode = ListNode(0)
        tmpNode = headNode
        heap = []
        
        for c,i in enumerate(lists):
            if i is None: continue
            heapq.heappush(heap,(i.val,c))
            
        while heap:
            val,index = heapq.heappop(heap)
            tmpNode.next = ListNode(val)
            tmpNode = tmpNode.next
            
            lists[index] = lists[index].next
            if lists[index] is not None:
                heapq.heappush(heap,(lists[index].val,index))
        return headNode.next