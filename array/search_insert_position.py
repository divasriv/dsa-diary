'''
Given a sorted arr of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
'''

from typing import List
# @lc app=leetcode id=35 lang=python3
# [35] Search Insert Position
# @lc code=start
class Solution:
    '''
    Given a sorted arr of distinct integers and a target value
    return the index if the target is found.
    '''
    def search_insert(self, nums: List[int], target: int) -> int:
        '''Return the index of the target if found
        else return the index where it would be inserted'''
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else: #nums[mid]>target
                r=mid-1
        return l

# @lc code=end
