class Solution:
    def lexicalOrder(self, n: int) -> list:
        datas = [[] for _ in range(10)]
        for i in range(1, n+1):
            s = str(i)
            datas[int(s[0])].append(s)

        for tmp in datas:
            tmp.sort()

        ans = []
        for tmp in datas:
            tmp = list(map(int, tmp))
            ans += tmp

        return ans

n = 13
ans = Solution().lexicalOrder(n)
print(ans)
