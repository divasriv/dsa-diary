'''
Problem:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Approach:
1. Create anagram_map dict
2. a dict has key:value.
for key, sort each word in str. => bat -> abt, nat ->ant, tan -> ant ...
3. add key in anagram_map if not present
4. else, apppend word to corresponding key
5. return *values* of the dict (inside a list)
'''
from typing import List
# @lc app=leetcode id=49 lang=python3
# [49] Group Anagrams
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map= {}
        for word in strs:
            key=''.join(sorted(word))
            if  key not in anagram_map:
                anagram_map[key] = []
            anagram_map[key].append(word)
        return list(anagram_map.values())

# @lc code=end
