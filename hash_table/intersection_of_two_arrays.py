'''
Problem:
Given two integer arrays nums1 and nums2, return an array of their intersection.

Example:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
[4,9] is also accepted.

Brute Force Approach:
convert to set, take intersection of both arrays (arr1 & arr2)
'''
from typing import List
# @lc app=leetcode id=349 lang=python3
# [349] Intersection of Two Arrays
# @lc code=start
class Solution:
    '''
    Given two integer arrays nums1 and nums2, return an array of their intersection.
    '''
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        return intersection array
        '''
        set1=set(nums1)
        set2=set(nums2)
        return list(set1&set2)

# @lc code=end
