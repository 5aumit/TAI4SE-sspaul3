#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.95%)
# Likes:    2372
# Dislikes: 1797
# Total Accepted:    718.5K
# Total Submissions: 2M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if not strs:
            return ''
        strs.sort(key=len)
        res = strs[0]
        while len(res) > 0:
            found = False
            for s in strs[1:]:               
                if res != s[:len(res)]:
                    res = res[:-1]
                    found = True
                    break
            if found:
                continue
            return res
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.longestCommonPrefix(["ca","a"])
    s.longestCommonPrefix(["dog","racecar","car"])
    s.longestCommonPrefix(["flower","flow","flight"])
