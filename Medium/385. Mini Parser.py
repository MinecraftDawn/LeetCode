# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s: return NestedInteger()

        if s[0] != "[": return NestedInteger(int(s))

        num = ""
        stack = [NestedInteger()]

        for char in s:
            if char == "[":
                stack.append(NestedInteger())
            elif char.isdigit() or char =="-":
                num += char
            elif char == ",":
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""
            elif char == "]":
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""
                stack[-2].add(stack.pop())

        return stack[0].getList()[0]