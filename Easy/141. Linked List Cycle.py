# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visted = {}
        run = head
        
        while run:
            if run not in visted:
                visted[run] = True
            else:
                return True
            run = run.next
            
        return False