'''
Problem:
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.
Then return the number of elements in nums which are not equal to val.

Example:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
'''
from typing import List
# @lc app=leetcode id=27 lang=python3
# [27] Remove Element
# @lc code=start
class Solution:
    '''
    Given an integer array nums and an integer val,
    remove all occurrences of val in nums in-place.
    '''
    def remove_element(self, nums: List[int], val: int) -> int:
        '''Remove all occurrences of val in nums'''
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k

# @lc code=end
