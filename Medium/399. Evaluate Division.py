from collections import defaultdict


class Solution:
    def calcEquation(self, equations: list, values: list, queries: list) -> list:
        graph = defaultdict(list)
        for i in range(len(equations)):
            d1, d2 = equations[i]
            val = values[i]
            graph[d1].append((d2, val))
            graph[d2].append((d1, 1 / val))

        def dfs(d1, d2, visted, curVal):
            if d1 == d2:
                return curVal

            if d1 in visted:
                return -1

            visted.add(d1)

            tmp = -1
            for child, val in graph[d1]:
                tmp = max(tmp,dfs(child, d2, visted, curVal * val))
            return tmp

        ans = []
        for d1, d2 in queries:
            if d1 in graph and d2 in graph:
                ans.append(dfs(d1, d2, set(), 1))
            else:
                ans.append(-1)

        return ans