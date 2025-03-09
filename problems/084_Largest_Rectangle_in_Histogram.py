from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        largest_area = 0
        stack = [0]
        for i, current_height in enumerate(heights[1:]):
            if heights[stack[-1]]
            current_area = current_height * num_rectagles

            largest_area = max(largest_area, current_area)
        return largest_area
