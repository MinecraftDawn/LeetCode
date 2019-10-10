# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head: return head
        
        nodes = []
        runNode = head
        
        while runNode:
            nodes.append(runNode)
            runNode = runNode.next
        
        nodes.sort(key=lambda node: node.val)
        
        preHead = ListNode(0)
        runNode = preHead
        for node in nodes:
            runNode.next = node
            runNode = runNode.next
            
        runNode.next = None
            
        return preHead.next