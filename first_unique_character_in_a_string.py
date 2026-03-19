from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        check = Counter(s)

        for index, letter in enumerate(s):
            if check[letter] == 1:
                return index
        return -1  