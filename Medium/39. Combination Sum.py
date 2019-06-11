class Solution:
    
    def combinationSum(self, candidates: list, target: int) -> list:
        candidates.sort()
        self.ans = []
        self.dfs(candidates,target,[])
        return self.ans
    
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
                self.dfs(candidates[count:],target-element,nextPath)