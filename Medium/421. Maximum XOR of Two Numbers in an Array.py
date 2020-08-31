class Node:
    def __init__(self):
        self.childs = [None, None]


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, num: str):
        cur = self.root
        for index in range(32):
            bit = int(num[index])
            if not cur.childs[bit]:
                cur.childs[bit] = Node()
            cur = cur.childs[bit]

        cur.isEnd = True

    def search(self, num: str):
        cur = self.root
        path = ""
        for index in range(32):
            if num[index] == "0":
                if cur.childs[1]:
                    path += "1"
                    cur = cur.childs[1]
                else:
                    path += "0"
                    cur = cur.childs[0]
            else:
                if cur.childs[0]:
                    path += "0"
                    cur = cur.childs[0]
                else:
                    path += "1"
                    cur = cur.childs[1]

        return int(num, 2) ^ int(path, 2)


class Solution:
    def findMaximumXOR(self, nums: list) -> int:
        trie = Trie()

        nums = [bin(num)[2:].zfill(32) for num in nums]

        for num in nums:
            trie.insert(num)

        maxValue = 0

        for num in nums:
            maxValue = max(maxValue, trie.search(num))

        return maxValue