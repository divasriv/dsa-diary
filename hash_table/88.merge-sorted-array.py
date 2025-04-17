'''
Problem:
nums1, nums2 sorted in asc order
m = number of elements in nums1
n = number of elements in nums2
Merge nums1 and nums2 inside array nums1.

Example:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Note for self:
The 0s are just placeholders at the end of nums1.
Not part of the actual data —  we need to overwrite them.
We need to USE m and n... not mentioned ainvayi

Brute force:
Pick up nums1 uptil m (after m is garbage), add nums2, sort to mix nums2 values in asc order
def merge(nums1, m, nums2, n):
    nums1[:] = nums1[:m] + nums2  # [:] to overwrite in-place
    nums1.sort()

Optimised:
Two pointer approach


'''
from typing import List
# @lc app=leetcode id=88 lang=python3
# [88] Merge Sorted Array
# @lc code=start
class Solution:
    '''
    Merge
    '''
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1  # pointer at end of nums1's valid elements
        j = n - 1  # pointer at end of nums2
        k = m + n - 1  # pointer at end of nums1's total length

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

# @lc code=end
