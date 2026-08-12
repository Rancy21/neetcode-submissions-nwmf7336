class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        max = 0
        while l < r:
            le = heights[l]
            ri = heights[r]
            diff = r - l
            w = 0
            if le > ri:
                w = diff * ri
                r -= 1
            elif le < ri:
                w = diff * le
                l += 1
            else:
                w = diff * ri
                l += 1
            
            if w > max:
                max = w

        return max
        