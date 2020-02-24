class Solution:
    def maxProduct(self, words: list) -> int:
        ans = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                word = words[j]
                for k in words[i]:
                    if k in word: break
                else:
                    ans = max(ans, len(word)*len(words[i]))
        return ans