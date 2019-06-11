class Solution:
    def combinationSum2(self, candidates: list, target: int) -> list:
        candidates.sort()
        self.ans = []
        self.dfs(candidates,target,[])
        
        a = [tuple(i) for i in self.ans]
        a = list(set(a))
        b = [list(i) for i in a]
        
        return b
    
    def dfs(self,candidates : list, target :int, path: list):
        if target == 0:
            self.ans.append(path)
            return
        
        for count,element in enumerate(candidates):
            if element > target:
                return
            else:
                nextPath = path.copy()
                nextPath.append(element)
                self.dfs(candidates[count+1:],target-element,nextPath)