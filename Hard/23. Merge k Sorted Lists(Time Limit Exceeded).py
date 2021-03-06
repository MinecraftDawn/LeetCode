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

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        linkList = LinkList()
        
        while len(lists):
            minNum = 100000000
            count = -1
            delList = []
            for c,i in enumerate(lists):
                if i is not None:
                    if i.val < minNum:
                        minNum = i.val
                        count = c
                else:
                    delList.append(c)
                    continue
            
            if count < 0 :break
                
            lists[count] = lists[count].next
            linkList.add(minNum)
            
            delList.reverse()
            for d in delList:
                del lists[d]
            
        return linkList.head