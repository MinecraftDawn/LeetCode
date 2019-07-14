class Solution:
    def fullJustify(self, words: list, maxWidth: int) -> list:
        ans = []
        left = 0
        preLeft = 0
        right = len(words)
        
        while left < right:
            curLen = 0
            i = 0
            for i in range(left,right):
                word = words[i]
                if curLen + len(word) + 1 > maxWidth + 1:
                    break
                else:
                    curLen += len(word) + 1
                    left += 1
                    
            count = 0
            if left == right:
                for i in range(preLeft,left-1):
                    words[i] += " "
                    count += 1
                words[left-1] += " " * (maxWidth - count - (curLen - (left-preLeft)))
            elif left - preLeft != 1:
                while count < maxWidth - (curLen - (left-preLeft)):
                    for i in range(preLeft,left-1):
                        words[i] += " "
                        count += 1
                        if count >= maxWidth - (curLen - (left-preLeft)): break
            else:
                words[preLeft] += " " * (maxWidth - len(words[preLeft]))
                    
            string = ""
            for i in range(preLeft,left):
                string += words[i]
                
            ans.append(string)
                
            preLeft = left
        
        return ans