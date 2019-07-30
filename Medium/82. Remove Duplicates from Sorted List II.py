# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import defaultdict

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        preNode = ListNode(0)
        
        nums = []
        tmp = head
        while tmp:
            nums.append(tmp.val)
            tmp = tmp.next
        
        if not nums:
            return None
        
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
            
        tmp = preNode
        for k,v in dic.items():
            if v == 1:
                tmp.next = ListNode(k)
                tmp = tmp.next
        
        return preNode.next