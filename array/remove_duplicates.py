'''
Problem:
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
Then return the number of unique elements in nums. (k)

Example:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5 (nums = [0,1,2,3,4,_,_,_,_,_])

Approach:
We can't use set(nums) because problem says "solve in-place", and set will take up extras space too.
We use two pointer approach here.
'''

from typing import List
# @lc app=leetcode id=26 lang=python3
# [26] Remove Duplicates from Sorted Array
# @lc code=start
class Solution:
    '''
    Given an integer array nums sorted in non-decreasing order,
    remove the duplicates in-place such that each unique element appears only once.
    The relative order of the elements should be kept the same.
    Then return the number of unique elements in nums.
    '''
    def remove_duplicates(self, nums: List[int]) -> int:
        '''Remove duplicates from sorted array'''
        k = 0
        if not nums:
            return k
        if len(nums) == 1:
            return len(nums)
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[k] = nums[i]
                k += 1
        nums[k] = nums[-1]
        return k + 1

# @lc code=end
