# Given a set of distinct positive integers, 
# find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.
# Given nums = [1,2,3], return [1,2] or [1,3]
# Given nums = [1,2,4,8], return [1,2,4,8]

class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset 
    """
    def largestDivisibleSubset(self, nums):
        if nums is None or len(nums) == 0:
            return []
        
        nums.sort()
        
        n = len(nums)
        dp = [1] * n
        # recording index of previous element
        father = [-1] * n
        
        # recording current max value and its index
        max_value, index = 0,-1
        
        for i in xrange(1,n):
            for j in xrange(0,i):
                if nums[i] % nums[j] == 0:
                    # if there is a j make dp[i] == dp[j] + 1, ignore this, as we get first sequence match the condition
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        father[i] = j
        
            if dp[i] > max_value:
                max_value = dp[i]
                index = i
        
        ans = [] 
        for i in xrange(max_value):
            ans.append(nums[index])
            index = father[index]
        
        return ans
            
