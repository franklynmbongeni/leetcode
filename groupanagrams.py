#the idea of this algorithm is that is first iterates thru the strings in strs
#and the inner loop will iterate thru the letters of the strings
#the count varible is important as it helps store the count for each letter for example 
# the string 'abcc' will update the count var to [1,1,2,0,0,0,0.....]
#and the string 'ccab' will also give the same output [1,1,2,0,0,0,0....]
#using this we can use the output to as a key but first we can to change it to  a tuple
#becouse a list is mutable there is not hashable so we can not use it as a key for defaultdict
#and the beautiful part about defaultdict is that if the a similar key already exists it just updates the values so we can use the .append()

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouper = defaultdict(list)

        for s in strs:
            count = [0] * 26 #we use this to store the count for the letters 
            for c in s:
                count[ord(c) - ord('a')] += 1 #the ord converts the letters to their numerical value and it updates the letter count to the var count
            key = tuple(count) # we have to change the count to a tuple if we want to use it as a key since a list is mutable therefore wont be hashable
            grouper[key].append(s)
        return list(grouper.values())
