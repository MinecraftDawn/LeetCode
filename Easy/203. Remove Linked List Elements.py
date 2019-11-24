# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        preHead = ListNode(0)
        preHead.next = head
        
        preNode = preHead
        while preNode.next:
            if preNode.next.val == val:
                preNode.next = preNode.next.next
            else:
                preNode = preNode.next

        return preHead.next