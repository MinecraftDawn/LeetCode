# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None: return None
        
        length = 1
        tmp = head
        while tmp.next:
            tmp = tmp.next
            length += 1
            
        tmp.next = head
        
        k %= length
        
        tmp = head
        for _ in range(length - k - 1):
            tmp = tmp.next
            
        newHead = tmp.next
        tmp.next = None