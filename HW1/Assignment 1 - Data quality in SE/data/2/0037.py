from typing import List

"""
1. Generate an array containing the products of all elements to the left of current element
2. Similarly, start from the last element and generate an array containing the products to the right of each element
3. Multiply both arrays element-wise

"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prod = 1
        # First generate the products to the left of the current element
        for num in nums:
            output.append(prod)
            prod *= num

        prod = 1
        # Now, generate and multiply the product to the right of current element
        for k in range(len(nums) - 1, -1, -1):
            output[k] = output[k] * prod
            prod *= nums[k]

        return output
