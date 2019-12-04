from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list) -> list:
        graph1 = defaultdict(set)
        graph2 = defaultdict(set)
        
        for curCls,preCls in prerequisites:
            graph1[preCls].add(curCls)
            graph2[curCls].add(preCls)
            
        ans = []
        notPre = [i for i in range(numCourses) if not graph2[i]]
        while notPre:
            curCls = notPre.pop()
            ans.append(curCls)
            
            for i in graph1[curCls]:
                graph2[i].remove(curCls)
                if not graph2[i]:
                    notPre.append(i)
            graph2.pop(curCls)
            
        return ans if not graph2 else []