#Intersection of Two Arrays II

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1) #this is a frequency counter it stores the result in a dictionery
        result = [] #this will be the output

        for num in nums2:
            if c[num] > 0: #this check the frequency if num is also available in the dictionery and the count is greater than zero then thats an intersaction
                result.append(num) #if there is an intersaction we add the result to RESULT
                c[num] -= 1 #we have to reduce the frequency since we added it to result
        return result
