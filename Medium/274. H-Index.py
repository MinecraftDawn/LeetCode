class Solution:
    def hIndex(self, citations: list) -> int:
        citations.sort(reverse=True)
        
        count = 0
        for i in range(len(citations)):
            if i < citations[i]:
                count += 1
            else:
                break
            
        return count