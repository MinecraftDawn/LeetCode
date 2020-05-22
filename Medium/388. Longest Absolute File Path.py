class Solution:
    def lengthLongestPath(self, input: str) -> int:
        path = input.split("\n")

        stack = []
        level = -1
        ans = 0
        for cur in path:
            curLevle = cur.count("\t")
            if curLevle == level+1:
                level += 1
                stack.append(len(cur)-curLevle)
            elif curLevle == level:
                stack.pop()
                stack.append(len(cur)-curLevle)
            elif curLevle < level:
                while curLevle <= level:
                    stack.pop()
                    level -= 1
                stack.append(len(cur)-curLevle)
                level += 1

            if cur.count("."):
                ans = max(ans, len(stack) - 1 + sum(stack))

        return ans