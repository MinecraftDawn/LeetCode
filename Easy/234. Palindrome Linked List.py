# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        runNode = head
        nodeList = []
        
        while runNode:
            nodeList.append(runNode.val)
            runNode = runNode.next
            
        for i in range(len(nodeList)//2 + len(nodeList) % 2):
            if nodeList[i] != nodeList[-i-1]:
                return False
            
        return True