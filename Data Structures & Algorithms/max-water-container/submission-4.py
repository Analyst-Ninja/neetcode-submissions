class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(1, n+1):
            for j in range(i , n+1):
                if i != j:
                    area = (j - i) * min(heights[i-1], heights[j-1])
                    max_area = max(area , max_area)

        return max_area
        