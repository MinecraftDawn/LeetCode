# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head

        stack = []
        preHead = Node(0, None, None, None)
        preHead.next = head
        run = head

        while True:
            if run.child:
                if run.next:
                    stack.append(run.next)
                run.next = run.child
                run.next.prev = run
                run.child = None

            if not run.next:
                if stack:
                    pop = stack.pop()
                    run.next = pop
                    run.next.prev = run
                else:
                    break

            run = run.next

        return preHead.next
