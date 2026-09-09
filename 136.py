#the solution uses bit manipulation , elements of the same value will cancel each other out
#and therefore the single number will be left this solution satisfy the constant space constraint 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res = num ^ res
        return res
    #further code explanation the ^ is an XOR operator it compared two numbers bBIT by BIT 
    # 5 = 101 and 3 = 011 3 = 011
    #5=  101
    #3=  011
    #   _____
    #    110
    #3=  011
    #   _____
    #    101
    #  so this means that similar number will cance each other out and the single number will be left behind  
