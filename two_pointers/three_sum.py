'''
Problem:
Given - integer array nums
Return distinct triplets [nums[i], nums[j], nums[k]]:
i != j, i != k, and j != k, nums[i] + nums[j] + nums[k] == 0

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''
from typing import List
# @lc app=leetcode id=15 lang=python3
# [15] 3Sum
# @lc code=start
class Solution:
    """3Sum problem
    """
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """3Sum problem
        Args:
            nums (List[int]): integer list

        Returns:
            List[List[int]]: [nums[i], nums[j], nums[k]], nums[i] + nums[j] + nums[k] == 0
        """
        nums.sort() #[-4,-1,-1,0,1,2]
        res=[]
        for i,num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue  # skip duplicate anchors
            l,r=i+1,len(nums)-1
            while l<r:
                total = num + nums[l] + nums[r]
                if total==0:
                    res.append([num,nums[l],nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l+=1
                    r-=1
                elif total<0:
                    l+=1
                else:
                    r-=1
        return res
# @lc code=end
s=Solution()
print(s.three_sum([-4, -2, -2, 0, 0, 1, 2, 2, 2, 3, 4]))
