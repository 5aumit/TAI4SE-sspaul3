#
# @lc app=leetcode.cn id=2006 lang=python3
#
# [2006] 差的绝对值为 K 的数对数目
#

# @lc code=start
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        def abs(x,y):
            if(x-y>=0):
                return x-y 
            else:
                return y-x 
        ret = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if(abs(nums[i],nums[j])==k):
                    ret += 1 
        return ret 
# @lc code=end

