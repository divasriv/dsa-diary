'''
Problem:
Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.
Do it *in-place* .

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Brute Force approach:
# write non zero elements to new_list, then push zeroes, then copy that to nums.

new_list=[]
n=len(nums)
for i in range(n):
    if nums[i]!=0:
        new_list.append(nums[i]) #non zero to new_list
#filling the rest with zeroes
result += [0] * (n - len(result))
# Copy back to original array (in-place part)
for i in range(n):
    nums[i] = result[i]

TC: O(n), SC: O(n)

Optimized approach:
Two pointer:
1. Use one pointer to iterate through the array. (for *i* in range(len(nums)))
2. Use another pointer to keep track of the position to place non-zero elements. (l=0)
3. When a non-zero element is found:
    if i != l, swap nums[i] with nums[l].
    otherwise, just increment l.
'''
from typing import List
# @lc app=leetcode id=283 lang=python3
# [283] Move Zeroes
# @lc code=start
class Solution:
    '''
    Given a non-empty array of digits representing a non-negative integer,
    increment one to the integer.
    '''
    def move_zeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != l:
                    nums[l], nums[i] = nums[i], nums[l]
                l += 1

# @lc code=end
