# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 15:20:27 2020

@author: Carol
"""

class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1.intersection(set2))