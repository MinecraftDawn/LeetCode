class Solution:
    def wiggleMaxLength(self, nums: list) -> int:
        mem = [[True, float("-inf"), 0],
               [False,float("inf"), 0]]
        
        for num in nums:
            for i in range(2):
                if mem[i][0]:
                    if num > mem[i][1]:
                        mem[i][1] = num
                        mem[i][2] += 1
                        mem[i][0] = not mem[i][0]
                    else:
                        mem[i][1] = num
                else:
                    if num < mem[i][1]:
                        mem[i][1] = num
                        mem[i][2] += 1
                        mem[i][0] = not mem[i][0]
                    else:
                        mem[i][1] = num
                
        
        return max(mem[0][2], mem[1][2])