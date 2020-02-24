class Solution:
    def maxProduct(self, words: list) -> int:
        ans = 0
        bitList = []
        
        for word in words:
            tmp = 0
            for char in word:
                tmp |= 1 << (ord(char) - 97)
            bitList.append(tmp)

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if bitList[i] & bitList[j] == 0:
                    ans = max(ans, len(words[i])*len(words[j]))
        
        return ans