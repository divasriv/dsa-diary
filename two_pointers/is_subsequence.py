"""
Problem:
Given two strings s and t, return true if s is a subsequence of t

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "ace", t = "abcde"
Output: true

Example 3:
Input: s = "aec", t = "abcde"
Output: false

Approach:
Traverse through t while maintaining a pointer for s.
Every time you find s[l] in t, move l to the next character in s.
If you reach the end of s, return True (all characters of s are found in order in t).
If you exhaust t and haven't finished s, return False
"""
# @lc app=leetcode id=392 lang=python3
# [392] Is Subsequence
# @lc code=start
class Solution:
    """ Find if s is subseq of t or not
    """
    def is_subsequence(self, s: str, t: str) -> bool:
        """ Find if s is subseq of t or not

        Args:
            s (str): substring
            t (str): main string

        Returns:
            bool: True or false depending on subsequence
        """
        l,r=0,0
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1  # move the pointer in s when a match is found
            r += 1  # always move the pointer in t
        return l == len(s)  # If l reached the end of s, it is a subsequence

# @lc code=end
