# -*- coding: utf-8 -*-
"""
Created on Sun May 26 18:29:45 2019

@author: Eric
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        string = ''
        for i in range(numRows):
            step1 = (numRows - 1) * 2
            step1 -= i * 2
            step2 = i * 2
            
            count = 1
            shoudPrint = True
            while i < len(s):
                if shoudPrint: string += s[i]
                if count % 2 == 1:
                    if i + step1 < len(s):
                        if step1 == 0: shoudPrint = False
                        else: shoudPrint = True
                        count += 1
                        i += step1
                    else: break
                else:
                    if i + step2 < len(s):
                        if step2 == 0: shoudPrint = False
                        else: shoudPrint = True
                        count += 1
                        i += step2
                    else: break
                        
        return string