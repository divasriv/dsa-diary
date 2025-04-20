'''
Problem:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Approach:
iterate thru both s & t,if all chars of s in t, return true.
    for i in range(len(s)):
        if s[i] not in t:
            return False
    return True

but it doesn't consider anagrams double characters...
if s = "aacc" and t = "ccac", this approach returns true, but it is false

 "anagram", t = "nagaram"
Optimised: Frequency mapping
1. create count dict
2. iterate over t:
    - if a char in t is not in count or it's count is 0, return false
    - otherwise keep decrementing char
Even better:
'''
# @lc app=leetcode id=242 lang=python3
# [242] Valid Anagram
# @lc code=start
class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        count={}
        for char in s:
            count[char]=count.get(char,0)+1
            #{a:3,n:1,g:1,r:1,m:1}
        for char_t in t:
            if char_t not in count or count[char_t]==0 :
                return False
            count[char_t]-=1
        return True

# @lc code=end

#dry run:
    # 'n': exists in count → 1 → 0
    # 'a': exists in count → 3 → 2
    # 'g': exists in count → 1 → 0
    # 'a': exists in count (again) → 2 → 1
    # 'r': exists in count → 1 → 0
    # 'a': exists in count (again) → 1 → 0
    # 'm': exists in count → 1 → 0
    # count= {'a': 0, 'n': 0, 'g': 0, 'r': 0, 'm': 0} -> Return True

