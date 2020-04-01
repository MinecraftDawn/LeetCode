class Solution:
    def reverseVowels(self, s: str) -> str:
        s2 = list(s)
        left,right = 0,len(s)-1
        
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        while left < right:
            while left < right and s2[left] not in vowel:
                left += 1
            
            while left < right and s2[right] not in vowel:
                right -= 1
                
            s2[left],s2[right] = s2[right],s2[left]
            left += 1
            right -= 1
            
        return "".join(s2)