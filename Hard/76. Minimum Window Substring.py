from collections import Counter,defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""
        
        strNum = defaultdict(int)
        tarNum = Counter(t)
        left = right = nums = ansLeft = 0
        ansRight = len(s)
        found = False
        
        for right in range(len(s)):
            strNum[s[right]] += 1
            
            if strNum[s[right]] == tarNum[s[right]]:
                nums += 1
             
            while nums == len(tarNum):
                if right - left < ansRight - ansLeft:
                    found = True
                    ansLeft,ansRight = left,right
                
                charL = s[left]
                strNum[charL] -= 1
                if strNum[charL] < tarNum[charL]:
                    nums -= 1
                left += 1
                
        if found: return s[ansLeft:ansRight+1]
        else: return ""