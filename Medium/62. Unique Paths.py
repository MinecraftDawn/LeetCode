class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        if m < n:
            m,n = n,m
            
        factorial = 1
        for i in range(n):
            factorial *= m+n-i
        for i in range(n):
            factorial /= n-i
        return int(factorial)