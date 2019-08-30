# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        tmp = head
        while tmp:
            nums.append(tmp.val)
            tmp = tmp.next
        
        root = self.sortedArrayToBST(nums)
        return root

    def sortedArrayToBST(self, nums: list) -> TreeNode:
        if not nums: return
        
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        
        return node