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