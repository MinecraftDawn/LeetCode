class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def invaild(num:str):
            return len(num) > 1 and num[0] == '0'
    
        for i in range(1, len(num)-1):         
            for j in range(i+1, len(num)):
                pre = num[:i]
                cur = num[i:j]
                if invaild(pre) or invaild(cur): continue
            
                while j < len(num):
                    nxt = str(int(pre) + int(cur))
                    if j + len(nxt) > len(num) or nxt != num[j:j+len(nxt)]: break
                    
                    j += len(nxt)
                    pre,cur = cur,nxt
                
                if j == len(num):
                    return True
        return False