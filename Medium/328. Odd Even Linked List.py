# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        tmp = []
        while head:
            tmp.append(head)
            head = head.next
        
        pre = ListNode(0)
        run = pre
        for i in range(0, len(tmp), 2):
            run.next = tmp[i]
            run = run.next
            
        for i in range(1, len(tmp), 2):
            run.next = tmp[i]
            run = run.next
        
        run.next = None
            
        return pre.next