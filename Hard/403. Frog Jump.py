class Solution:
    def canCross(self, stones: list) -> bool:
        if stones[0] != 0 or stones[1] != 1: return False

        self.end = stones[-1]
        self.stones = set(stones)
        self.visted = {}

        return self.jump(0, 1)

    def jump(self, cur: int, step: int):
        if cur == self.end: return True

        if (cur, step) in self.visted:
            return self.visted[(cur, step)]

        for i in range(max(step - 1, 1), step + 2):
            if cur + i in self.stones:
                arrival = self.jump(cur + i, i)
                self.visted[(cur + i, i)] = arrival
                if arrival:
                    return True

        return False