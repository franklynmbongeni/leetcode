class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        """

        j = len(s) - 1
        i = 0

        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        #this solution runs at at o(n) time and uses o(1) space


#the second solution


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        """

        s[:] = s[::-1] #this solution looks great as it is short however it uses o(n) space because of slicing