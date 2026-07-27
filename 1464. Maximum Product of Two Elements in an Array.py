class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        first = second = 0
        for x in nums:
            if x >= first:
                second = first
                first = x
            elif x > second:
                second = x
        return (first - 1) * (second - 1)