class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        dummy = [0 for _ in nums]

        for i in range(len(nums)):
            dummy[(i + k) % len(nums)] = nums[i]

        nums[:] = dummy