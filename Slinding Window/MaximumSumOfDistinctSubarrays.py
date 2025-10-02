"""
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.
"""


class Solution:

    
    def maximumSubarraySum(self, nums, k):
        start = 0
        maximumSubarraySum = 0
        for start in range(len(nums) - k):
            #verifying unique elements
            copynums=set(nums[start:k+start])
            if len(nums[start:k+start]) == len(copynums):
                #Calcuating the 
                if sum(nums[start: k+start]) > maximumSubarraySum:
                    maximumSubarraySum = sum(nums[start: k+start])
        return maximumSubarraySum

            
    
    
    
sol = Solution()
sol.maximumSubarraySum([1,5,4,2,9,9,9], k=3)