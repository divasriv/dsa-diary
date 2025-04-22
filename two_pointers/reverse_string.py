'''
Problem:
Write a function that reverses a string.
The input string is given as an array of characters s.
You must do this by modifying the input array in-place
with O(1) extra memory.

Approach:
s.reverse() or two pointer
'''
from typing import List
# @lc app=leetcode id=344 lang=python3
# [344] Reverse String
# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r=0,len(s)-1
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        # or
        # s.reverse()
# @lc code=end

