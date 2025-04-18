'''
Problem:
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays.

Example:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Brute Force Approach:
Cannot convert to set here, since we will lose the duplicate elements.
Cannot do nums1 & nums2 because '&' operation is not defined for lists.
So, we copy list2 as list2_copy(so that real list2 is safe), iterate thru list1, if num found in list2, append to intersection arr and remove from copy.  when copy=empty, return intersection arr.
TC - O(n**2)

Optimised Approach:
Use hashmap (freq counter/ count array), count how many times num is in nums1
iterate over nums2 -
    if num is in nums2, add to result arr
    remove one count of num from count array
TC - O(n + m), NOT O(n**2)
'''
from typing import List
# @lc app=leetcode id=350 lang=python3
# [349] Intersection of Two Arrays II
# @lc code=start
class Solution:
    '''return intersection arr, all occurences of elements in arr1 and arr2 should be present'''
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''creating intersect arr'''
        counts={}
        res=[]
        for num in nums1:
            counts[num]=counts.get(num,0)+1
        for num in nums2:
            if counts.get(num, 0)>0:    #same as counts[num]>0,
                                        #but won't give KeyError if num not in counts, will return 0
                res.append(num)
                counts[num]-=1
        return res

# @lc code=end
