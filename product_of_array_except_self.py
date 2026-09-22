class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [0] * len(nums)

        for i in range(len(nums)):
            temp = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                dummy = nums[j]
                temp *= dummy
            output[i] = temp
        return output
    ## this above solution works however it is not efficient as it uses O(n2) time because it loops over the numbers
