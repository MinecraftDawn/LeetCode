from collections import defaultdict


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        hashMap = defaultdict(list)

        for i in range(1, n + 1):
            i = str(i)
            hashMap[i[0]].append(i)

        i = 1
        while k > 0:
            if len(hashMap[str(i)]) >= k:
                return sorted(hashMap[str(i)])[k - 1]
            else:
                k -= len(hashMap[str(i)])
                i += 1