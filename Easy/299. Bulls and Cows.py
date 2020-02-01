from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = B = 0
        secretMap = defaultdict(int)
        guessMap = defaultdict(int)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                secretMap[secret[i]] += 1
                guessMap[guess[i]] += 1
                
        for k,v in secretMap.items():
            B += min(v, guessMap[k])

        return str(A)+"A" + str(B)+"B"