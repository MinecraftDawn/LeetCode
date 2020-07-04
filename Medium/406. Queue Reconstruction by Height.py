from collections import defaultdict
import bisect

class Solution:
    def reconstructQueue(self, people: list) -> list:
        ans = []
        peoDict = defaultdict(list)
        
        for p in people:
            bisect.insort_left(peoDict[p[1]], p[0])
        
        keys = sorted(peoDict.keys())
        
        
        for key in keys:
            last = 0
            for item in peoDict[key]:
                bigger = key
                i = 0
                for i in range(len(ans)):
                    if ans[i][0] >= item:
                        bigger -= 1
                    if bigger == 0:
                        break
                i += 1
                
                if i <= last:
#                    print(item, i)
                    i = last + 1
                ans.insert(i, [item, key])
                last = i
        
#        print(ans)
            
        return ans