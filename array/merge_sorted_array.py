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
        i=m-1   #first pointer at end of nums1 (till real values)
        j=n-1   #second pointer at end of nums2
        k=(m+n)-1   #third pointer at end of nums1 (extra space/ 0's)
        while j>=0: #while j pointer not at start of nums2
            if i>=0 and nums1[i]>nums2[j]: #if i pointer not at start of nums2 and nums1[i]>nums2[j]
                nums1[k]=nums1[i] #put nums1[i] at end of nums1
                i-=1 #move i to left
            else: #nums2[j]>nums1[i]
                nums1[k]=nums2[j] #put nums1[i] at end of nums1
                j-=1 #move j to left
            k-=1 #move k to left 0, run loop again
        #no return cuz in-place merge, but return nums1 would give sorted nums1

# @lc code=end
