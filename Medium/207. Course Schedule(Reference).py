<<<<<<< HEAD
# Reference: https://leetcode.com/problems/course-schedule/discuss/441722/Python-99-time-and-100-space.-Collection-of-solutions-with-explanation
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list) -> bool:
        graph = [[] for _ in range(numCourses)]
        
        for curCls,preCls in prerequisites:
            graph[preCls].append(curCls)
            
        cycle = [0] * numCourses
        
        def hasCycle(node: int):
            if cycle[node] == -1:
                return False
            elif cycle[node] == 1:
                return True
            else:
                cycle[node] = 1
                
                for i in graph[node]:
                    if hasCycle(i):
                        return True
                cycle[node] = -1
                return False               
            
        for node in range(numCourses):
            if hasCycle(node): return False
            
=======
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list) -> bool:
        graph = {}
        self.cycle = False
        
        for cur,pre in prerequisites:
            if cur not in graph:
                graph[cur] = set([pre])
            else:
                graph[cur].add(pre)
        
        def isCycle(curClass, curSet):
            if self.cycle: return
            
            if curClass in graph:
                for preClass in graph[curClass]:
                    if preClass in curSet:
                        self.cycle = True
                    else:
                        curSet.add(preClass)
                        isCycle(preClass, curSet)
                        
            curSet.remove(curClass)
            
        for curClass in graph.keys():
            curSet = set([curClass])
            self.cycle = False
            isCycle(curClass, curSet)
            if self.cycle:
                return False
>>>>>>> 86fa52cdee82e9705253a0a7b7d0c8defdcf9467
        return True