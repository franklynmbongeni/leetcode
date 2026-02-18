#the solution uses bit manipulation , elements of the same value will cancel each other out
#and therefore the single number will be left

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res = num ^ res
        return res