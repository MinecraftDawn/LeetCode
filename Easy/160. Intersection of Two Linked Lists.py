# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        visted = {}
        run = headA
        
        while run:
            visted[run] = True
            run = run.next
            
        run = headB
        while run:
            if run in visted:
                return run
            run = run.next
        return None