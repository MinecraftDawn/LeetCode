from functools import lru_cache


class Solution:
    def canCross(self, stones: list) -> bool:
        if stones[0] != 0 or stones[1] != 1: return False

        self.end = stones[-1]
        self.stones = set(stones)

        return self.jump(0, 1)

    @lru_cache(None)
    def jump(self, cur: int, step: int):
        if cur == self.end: return True

        for i in range(max(step - 1, 1), step + 2):
            if cur + i in self.stones and self.jump(cur + i, i):
                return True

        return False