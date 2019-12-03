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
        return True