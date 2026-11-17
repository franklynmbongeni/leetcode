""""class Solution:
    def maxArea(self, heights: List[int]) -> int:

        answer = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                width = abs(i - j)
                height = min(heights[i], heights[j])
                area = width * height
                answer = max(answer , area)
        return answer"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        answer = 0

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            area = height * width
            answer = max(answer , area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return answer
