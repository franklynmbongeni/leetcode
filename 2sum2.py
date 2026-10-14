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
        
