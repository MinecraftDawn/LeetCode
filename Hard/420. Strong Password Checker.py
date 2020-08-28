class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        if len(s) <= 20:
            tmp = 0
            for rep in self.repectModify(s):
                tmp += rep // 3
            return max(6 - len(s), self.caseNum(s), tmp)
        else:
            # Reference: https://leetcode.com/problems/strong-password-checker/discuss/795451/Fastest-Python-Solution-8ms
            delta = len(s) - 20
            rep = self.repectModify(s)
            n = 0
            while n < delta:
                found = False
                for i in range(len(rep)):
                    newRep = []
                    for j in range(len(rep)):
                        if rep[i] >= 3:
                            newRep.append(rep[i])
                    if not newRep:
                        break
                    if rep[i] == min(newRep, key=lambda x: x % 3):
                        found = True
                        rep[i] -= 1
                        n += 1
                        if n >= delta:
                            break
                if not found:
                    break
            repleft = sum(c // 3 for c in rep)
            return delta + max(repleft, self.caseNum(s))

    def caseNum(self, s: str) -> list:
        case = [False] * 3
        for char in s:
            ascii = ord(char)
            if 48 <= ascii <= 57:
                case[2] = True
            elif 65 <= ascii <= 90:
                case[1] = True
            elif 97 <= ascii <= 122:
                case[0] = True
        return 3 - sum(case)

    def repectModify(self, s: str):
        pre = " "
        conti = 0
        ans = []
        s += " "
        for char in s:
            if pre == char:
                conti += 1
            else:
                if conti >= 3:
                    ans.append(conti)
                conti = 1
            pre = char
        return ans