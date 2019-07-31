# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None
        
        run = head
        while run and run.next:
            if run.val == run.next.val:
                run.next = run.next.next
            else:
                run = run.next
                
        return head