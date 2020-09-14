from collections import defaultdict


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = defaultdict(int)

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        self.dict[key] += 1

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        self.dict[key] -= 1
        if self.dict[key] <= 0:
            del self.dict[key]

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        string = ""
        value = float("-inf")
        for k,v in self.dict.items():
            if v > value:
                value = v
                string = k
        return string

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        string = ""
        value = float("inf")
        for k, v in self.dict.items():
            if v < value:
                value = v
                string = k
        return string

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
