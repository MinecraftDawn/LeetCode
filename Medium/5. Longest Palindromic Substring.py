class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        for i in range(1,len(s)):
            for j in range(len(s)//2+1):
                if i-j < 0 or i+j > len(s)-1: break
            
                if s[i-j] == s[i+j]:
                    if len(s[i-j:i+j+1]) > len(longest):
                        longest = s[i-j:i+j+1]
                else:
                    break
            
            if s[i-1] == s[i]:
                for j in range(len(s)//2):
                    if i-1-j < 0 or i+j > len(s)-1:break
                
                    if s[i-1-j] == s[i+j]:
                        if len(s[i-1-j:i+j+1]) > len(longest):
                            longest = s[i-1-j:i+j+1]
                    else: break
                            
        if longest == '' and len(s) > 0: longest = s[0]
        return longest
            