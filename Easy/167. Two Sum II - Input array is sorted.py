import bisect
class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        for index,num1 in enumerate(numbers):
            index2 = bisect.bisect_left(numbers,target-num1,index+1,len(numbers)-1)
            if num1+numbers[index2] == target:
                return [index+1,index2+1]