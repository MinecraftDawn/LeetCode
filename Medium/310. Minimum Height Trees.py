from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: list) -> list:
        if not edges: return [0]
        path = defaultdict(list)
        
        for p1,p2 in edges:
            path[p1].append(p2)
            path[p2].append(p1)
        
        ans = []
        
        for i in path.keys():
            visted = set()
            queue = [[i],[]]
            deep = 0
            while queue[0]:
                cur = queue[0].pop(0)
                visted.add(cur)
                for j in path[cur]:
                    if j not in visted:
                        queue[1].append(j)
                        
                if not queue[0]:
                    deep += 1
                    queue[0],queue[1] = queue[1],queue[0]
                    
            if not ans:
                ans.append(deep)
                ans.append(i)
            elif ans[0] == deep:
                ans.append(i)
            elif ans[0] > deep:
                ans = []
                ans.append(deep)
                ans.append(i)

        return ans[1:]