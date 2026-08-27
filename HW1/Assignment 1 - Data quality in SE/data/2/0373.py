# most straightforward solution would be more efficient with multiple return values, and Python makes those easy to handle

def tilt_and_sum(node):
    if node == None:
        return (0,0)
    left_sum, left_tilt = tilt_and_sum(node.left)
    right_sum, right_tilt = tilt_and_sum(node.right)
    return (node.val + left_sum + right_sum, abs(left_sum-right_sum) + left_tilt + right_tilt)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        full_sum, full_tilt = tilt_and_sum(root)
        return full_tilt
