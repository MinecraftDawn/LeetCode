# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        nodes = []
        
        run = head
        while run:
            nodes.append(run)
            run = run.next
        
        preHead = ListNode(0)
        run = preHead
        while nodes:
            run.next = nodes.pop()
            run = run.next
        run.next = None
            
        return preHead.next
        
