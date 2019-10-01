"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        self.table = {}
        self.table[None] = None
        newHead = self.buildList(head)
        
        runOld = head
        runNew = newHead
        while runNew:
            runNew.random = self.table[runOld.random]
            runNew = runNew.next
            runOld = runOld.next
        return newHead
    
    def buildList(self, node: 'Node') -> 'Node':
        if not node: return
        new = Node(node.val, self.buildList(node.next), None)
        self.table[node] = new
        return new
        