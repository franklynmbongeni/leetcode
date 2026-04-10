class Solution:
    def reverse(self, x: int) -> int:
        # variables to check overflow
        max = 2 ** 31 - 1
        min = -2 ** 31

        reversed_num = 0

        while x != 0:
            digit = int(math.fmod(x, 10)) #this keeps the result sign the same (i had used x % 10 which results in -1 % 10 = 9)
            x = int(x / 10)

            if (reversed_num > max // 10 or
                    (reversed_num == max // 10 and digit >= max % 10)):
                return 0

            if (reversed_num < min // 10 or
                    (reversed_num == min // 10 and digit <= min % 10)):
                return 0

            reversed_num = reversed_num * 10 + digit

        return reversed_num