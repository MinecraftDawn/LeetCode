class Solution:
    def lastRemaining(self, n: int) -> int:
        tmp = [x for x in range(1, n+1)]
        direct = True

        while len(tmp) != 1:
            tmp2 = []
            if direct:
                for i in range(1, len(tmp), 2):
                    tmp2.append(tmp[i])
            else:
                for i in range(len(tmp)-2, -1, -2):
                    tmp2.append(tmp[i])
                tmp2.reverse()

            direct = not direct
            tmp = tmp2

        return tmp[0]