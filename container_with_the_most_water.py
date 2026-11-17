class Solution:
    def maxArea(self, heights: List[int]) -> int:

        answer = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                width = abs(i - j)
                height = min(heights[i], heights[j])
                area = width * height
                answer = max(answer , area)
        return answer