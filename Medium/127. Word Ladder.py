from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list) -> list:
        if endWord not in wordList: return 0
        
        queue = [[],[]]
        ans = []
        visted = set([])
        
        myDict = defaultdict(set)
        for word in wordList:
            for i in range(len(beginWord)):
                myDict[word[:i] + "*" + word[i+1:]].add(word)
                
        for i in range(len(beginWord)):
            for word in myDict[beginWord[:i] + "*" + beginWord[i+1:]]:
                if word != beginWord:
                    queue[0].append((word, [beginWord]))

        while queue[0]:
            nowItem = queue[0].pop()
            word, prePath, = nowItem
            path = prePath.copy()
            path.append(word)
            visted.add(word)
            
            if word == endWord:
                return len(path)
            else:
                for i in range(len(beginWord)):
                    for nextWord in myDict[word[:i] + "*" + word[i+1:]]:
                        if nextWord not in path and nextWord not in visted:
                            queue[1].append((nextWord, path))
            
                if not queue[0] and not ans:
                    queue[0],queue[1] = queue[1],queue[0]
        return 0