'''
leetCode 54: Maximum Subarray:https://leetcode.com/problems/maximum-subarray
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSub=nums[0]
        currSum=0
        for n in nums:
            if currSum<0:
                currSum=0
            currSum+=n
            maxSub=max(maxSub,currSum)# make it 54 ms run time
            #alternative of max function is if else statement that make it 18ms runvtime
            '''
            
            if maxSub >currSum:
                maxSub=maxSub
            else:
                maxSub=currSum
            '''
        return maxSub
        