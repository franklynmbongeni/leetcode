class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        #brute force O(n2) solution

        result = []

        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                total = numbers[i] + numbers[j] 
                if total == target:
                    result.append(i + 1)
                    result.append(j + 1)
                    return result
        # efficient solution

        l,r = 0, len(numbers) -1

        while l < r:
            cursum = numbers[l] + number[r]
            if cursum == target:
                return [l + 1, r + 1]
            elif cursum > target:
                r -= 1
            else:
                l += 1

        #explanation for the solution
        #since the input is sorted it means we can use two pointer one at the start and the other at the end 
        #by this we can compare the the total of the two if its bigger than the target we can decreament the r pointer which is at the end
        #therefore meaning we reduce the total if our total was too small we can increament the l pointer which therefore means we increase the total 
        # threfore we will get closer to the target number (sidenote it basically treating the input as a numberline a quite interesting solution honestly)
        
