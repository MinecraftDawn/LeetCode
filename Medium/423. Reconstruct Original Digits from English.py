from collections import Counter


class Solution:
    def __init__(self):
        self.ENGLISH = ("zero", "one", "two", "three", "four",
                        "five", "six", "seven", "eight", "nine")

    def originalDigits(self, s: str) -> str:
        a_z = Counter(s)
        numCount = [0] * 10

        self.decrease(a_z, numCount, 0, 'z')
        self.decrease(a_z, numCount, 2, "w")
        self.decrease(a_z, numCount, 4, "u")
        self.decrease(a_z, numCount, 5, "f")
        self.decrease(a_z, numCount, 6, "x")
        self.decrease(a_z, numCount, 7, "s")
        self.decrease(a_z, numCount, 8, "g")
        self.decrease(a_z, numCount, 9, "i")
        self.decrease(a_z, numCount, 1, "o")
        self.decrease(a_z, numCount, 3, "r")

        ans = ""
        for i in range(10):
            ans += str(i) * numCount[i]

        return ans

    def decrease(self, a_z: Counter, numCount: list, num: int, key):
        numCount[num] = a_z[key]
        for c in self.ENGLISH[num]:
            a_z[c] -= numCount[num]