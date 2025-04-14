'''
LeetCode 217. Contains Duplicate
Given an integer array nums, return true if any value appears
at least twice in the array, and return false if every element is distinct.
Example 1:
Input: nums = [1,2,3,1]
Output: true
'''
# @lc app=leetcode id=217 lang=python3
# [217] Contains Duplicate
# @lc code=start
from typing import List
class Solution:
    '''
    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.
    '''
    def contains_duplicate(self, nums: List[int]) -> bool:
        '''Return true if any value appears at least twice in the array'''
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return True
            hashmap[num] = 1
        return False
# @lc code=end
