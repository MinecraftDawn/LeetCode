# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        def reverseNode(preHead: ListNode,reverse: list,k: int):
            preHead.next = reverse[k-1]
            
            reverse[0].next = reverse[k-1].next
            
            for i in range(k-1,0,-1):
                reverse[i].next = reverse[i-1]
            
                
        unusefulNode = ListNode(0)
        unusefulNode.next = head
        
        if head is None: return head
        if head.next is None: return head
        
        
        runNode = unusefulNode
        preHead = runNode
        
        while runNode.next is not None:
            myList = []
            preHead = runNode
            
            for _ in range(k):
                if runNode.next is None: break
                
                runNode = runNode.next
                tmpNode = runNode
                myList.append(tmpNode)
            
            if len(myList) == k:
                reverseNode(preHead,myList,k)
            
            for _ in range(k-1):
                if runNode.next is None: break
                runNode = runNode.next
        
        return unusefulNode.next