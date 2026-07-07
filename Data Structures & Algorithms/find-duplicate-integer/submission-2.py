class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}

        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                return i