#two sum leetcode problem


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        check = {} # dictionery

        for i in range(len(nums)):
            diff = target - nums[i] #the diff is to check if there is a number that when added with the current i can add up to the target
            if diff in check: #this check is constant time
                return [i, check[diff]] #if the DIFFerence is found we return the indices of the number
            check[nums[i]] = i #this if for when the difference is not found we add a key which is the number and the value will be the indice this will take O(1) time