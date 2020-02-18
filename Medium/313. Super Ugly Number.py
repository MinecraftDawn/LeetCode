class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list) -> int:
        ans = [1]
        primeCount = [0] * len(primes)
        mul = primes.copy()
        count = 1
        
        while count < n:
            tmp = min(mul)
            ans.append(tmp)
            count += 1
            for i,val in enumerate(mul):
                if tmp == val:
                    primeCount[i] += 1
                    mul[i] = ans[primeCount[i]] * primes[i]
        
        return ans[-1]