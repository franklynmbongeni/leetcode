"first solution "
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        check = Counter(nums)

        for item in check.most_common(k): #most_common will return a tuple (x,y) 
            result.append(item[0])
        return result
