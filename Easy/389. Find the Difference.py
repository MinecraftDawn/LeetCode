from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = Counter()

        for char in t:
            counter[char] += 1

        for char in s:
            counter[char] -= 1


        return list(counter.elements())[0]