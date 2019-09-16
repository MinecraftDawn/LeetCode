class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list) -> list:
        if endWord not in wordList: return []
        ans = []
        queue = [[[beginWord, wordList, []]], []]
        while queue[0]:
            nowItem = queue[0].pop()
            begWord = nowItem[0]
            wList = nowItem[1]
            usedWord = nowItem[2]
            
            if self.canTransform(begWord,endWord):
                ans.append([beginWord] + usedWord + [endWord])
                
            else:
                for index,word in enumerate(wList):
                    if self.canTransform(begWord, word):
                        tmp = wList[:index] + wList[index+1:]
                        tmp2 = usedWord[::]
                        tmp2.append(word)
                        queue[1].append([word, tmp, tmp2])
            
                if not queue[0] and not ans:
                    queue[0],queue[1] = queue[1],queue[0]
        return ans
                
    def canTransform(self, word1, word2):
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
        return diff == 1