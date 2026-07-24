class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        MAX = 2048

        s = set(nums)

        pair_xors = set()
        for a in nums:
            for b in nums:
                pair_xors.add(a ^ b)

        result = set()
        for ab in pair_xors:
            for c in s:
                result.add(ab ^ c)

        return len(result)