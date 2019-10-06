# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        
        nodes = []
        run = head.next
        while run:
            nodes.append(run)
            run = run.next
            
        run = head
        while nodes:
            run.next = nodes.pop()
            run = run.next
            if nodes:
                run.next = nodes.pop(0)
                run = run.next
        run.next = None