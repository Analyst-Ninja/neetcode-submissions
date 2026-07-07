class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = 0
        r = n - 1

        valKeyMap = {}
        for i in range(n):
            first = nums[i]
            second = target - nums[i]
            if second in valKeyMap:
                return[valKeyMap[second], i]
            valKeyMap[first] = i 

        return []
        