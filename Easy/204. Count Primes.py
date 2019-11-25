class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True] * (n)
        
        for i in range(2, int(n ** 0.5)+1):
            if not primes[i]: continue
            for j in range(i**2, n, i):
                primes[j] = False
               
        count = 0
        for i in range(2, n):
            if primes[i]:
                count += 1
        return count
        ans = []
        for i in range(2, n):
            if not primes[i]: continue
            ans.append(i)

        return ans