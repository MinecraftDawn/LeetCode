# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head: return None
        
        small = []
        big = []
        
        tmp = head
        while tmp:
            if tmp.val < x: small.append(tmp.val)
            else: big.append(tmp.val)
            tmp = tmp.next
            
        preHead = ListNode(0)
        tmp = preHead
        while small:
            tmp.next = ListNode(small.pop(0))
            tmp = tmp.next
            
        while big:
            tmp.next = ListNode(big.pop(0))
            tmp = tmp.next
            
        return preHead.next