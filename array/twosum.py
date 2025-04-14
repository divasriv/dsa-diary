'''
Problem:
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Approach:
Using a hash map (dictionary) to store each index.
For each number, check if diff (target - num) is already in the dictionary.
If it is, we've found our pair, return indexes of diff and num.
If not found, return -1.
'''
from typing import List
# @lc app=leetcode id=1 lang=python3
# [1] Two Sum
# @lc code=start
class Solution:
    '''
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.
    '''
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        '''Return indices of the two numbers such that they add up to target'''
        hashmap={}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return hashmap[diff], i
            hashmap[num] = i
        return -1

# @lc code=end
