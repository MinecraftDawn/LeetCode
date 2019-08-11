# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        preHead = ListNode(0)
        preHead.next = head
        nodeList = []
        
        reHead = preHead
        for i in range(m - 1):
            reHead = reHead.next
        pre = reHead
        reHead = reHead.next
        
        for i in range(n-m):
            nodeList.append(reHead)
            reHead = reHead.next
        
        tail = reHead.next
        
        pre.next = reHead
        
        tmp = reHead
        while nodeList:
            tmp.next = nodeList.pop()
            tmp = tmp.next
        
        tmp.next = tail
            
        return preHead.next