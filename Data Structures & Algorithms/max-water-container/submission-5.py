class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # n = len(heights)
        # max_area = 0
        # # brute force methode
        # for i in range(1, n+1):
        #     for j in range(i , n+1):
        #         if i != j:
        #             area = (j - i) * min(heights[i-1], heights[j-1])
        #             max_area = max(area , max_area)

        # Two pointer approach
        l = 0
        r = len(heights) - 1
        n = len(heights)
        max_area = 0

        for i in range(n):
            area = (r - l) * min(heights[l], heights[r])
            max_area = max(max_area, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
            if l == r:
                break

        return max_area
        