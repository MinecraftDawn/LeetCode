from functools import cmp_to_key


class Solution:
    def reconstructQueue(self, people: list) -> list:
        people = sorted(people, key=cmp_to_key(self.cmp))
        ans = []

        for p in people:
            ans.insert(p[1], p)

        return ans

    def cmp(self, a: list, b: list):
        if a[0] > b[0]:
            return -1
        elif a[0] < b[0]:
            return 1
        else:
            if a[1] < b[1]:
                return -1
            else:
                return 1