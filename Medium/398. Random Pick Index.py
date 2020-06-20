from collections import defaultdict
import random


class Solution:

    def __init__(self, nums: list):
        self.dict = defaultdict(list)
        for index, num in enumerate(nums):
            self.dict[num].append(index)

    def pick(self, target: int) -> int:
        return random.choice(self.dict[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)