# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        
        newHead = head.next
        head.next = newHead.next
        newHead.next = head
        
        leftNode = head
        if leftNode.next is None: return newHead
        if leftNode.next.next is None: return newHead
        midNode = leftNode.next
        rightNode = midNode.next
        while midNode is not None and rightNode is not None:
            leftNode.next = rightNode
            midNode.next = rightNode.next
            rightNode.next = midNode
            
            leftNode = midNode
            if midNode.next is None: break
            midNode = midNode.next
            if midNode.next is None: break
            rightNode = midNode.next
        return newHead
        