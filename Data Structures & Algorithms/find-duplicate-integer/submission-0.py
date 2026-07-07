class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = [0] * len(nums)

        for num in nums:
            if seen[num]:
                return num

            seen[num] = 1