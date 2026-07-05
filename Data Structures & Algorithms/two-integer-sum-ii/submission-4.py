class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        n = len(numbers)

        for i in range(n):
            if numbers[start] + numbers[end] == target and start != end:
                return [start+1, end+1]
            elif numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1
        return []
        