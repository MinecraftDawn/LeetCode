# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class LinkList:
    def __init__(self):
        self.head = None
        self.nodeNum = 0
        
    def add(self,value):
        if self.head is None:
            self.head = ListNode(value)
        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = ListNode(value)
            
    def trace(self):
        if self.head is None: return
        
        tmp = self.head
        while tmp.next is not None:
            print(tmp.val)
            tmp = tmp.next
        print(tmp.val)
        
    def countNode(self):
        self.nodeNum = 0
        tmp = self.head
        while tmp.next is not None:
            self.nodeNum += 1
            tmp = tmp.next
        self.nodeNum += 1
        
    def remove(self,index):
        self.countNode()
        index = self.nodeNum - index
        if index == 0:
            if self.head.next is not None:
                self.head = self.head.next
            else:
                self.head = None
        else:
            if self.head.next is not None:
                preNode = self.head
                nextNode = self.head.next
                
                i = 1
                while nextNode.next is not None:
                    if i == index:
                        preNode.next = nextNode.next
                        break
                    preNode = nextNode
                    nextNode = nextNode.next
                    i += 1
                    
                if i == index:
                    if nextNode.next is None:
                        preNode.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged = LinkList()
        while l1 is not None and l2 is not None:
            val1 = l1.val
            val2 = l2.val
            
            if val1 < val2:
                merged.add(val1)
                l1 = l1.next
            else:
                merged.add(val2)
                l2 = l2.next
        
        while l1 is not None:
            merged.add(l1.val)
            l1 = l1.next
        
        while l2 is not None:
            merged.add(l2.val)
            l2 = l2.next
        
        return merged.head
        