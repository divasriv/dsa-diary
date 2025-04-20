'''
Problem:
Given two strings s and t, determine if they are isomorphic

Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'
Mapping 'g' to 'd'

Example 2:
Input: s = "foo", t = "bar"
Output: false
Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Approach:

Two hashmaps (dicts), s_to_t, t_to_s
check if both strings are of equal length
iterate thru BOTH strings (zip.)
for each character:
    - If it's not already mapped, map it    #s_to_t[char_s] = char_t
    - If it's already mapped but not to the correct character, return False     #if s_to_t[char_s] != char_t or vice versa, return false
    - if no errors till loop end, return True
'''
# @lc code=start
# @lc app=leetcode id=205 lang=python3
# [205] Isomorphic Strings
# @lc code=start
class Solution:
    def is_isomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_to_t, t_to_s={},{}
        for char_s, char_t in zip(s,t):
            if (char_s in s_to_t and s_to_t[char_s] != char_t) or (char_t in t_to_s and t_to_s[char_t] != char_s):
                return False
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s
        return True

# @lc code=end

