# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class LinkList:
    def __init__(self):
        self.head = None
        
    def add(self,value):
        if self.head is None:
            self.head = ListNode(value)
        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = ListNode(value)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        linkList = LinkList()
        while l1 is not None and l2 is not None:
            linkList.add((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            linkList.add((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            l1 = l1.next
        while l2 is not None:
            linkList.add((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            l2 = l2.next
        if carry > 0:
            linkList.add(carry)
        return linkList.head