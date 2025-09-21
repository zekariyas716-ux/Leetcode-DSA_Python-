class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        reversed_number = 0
        if x < 0:
            return False
        else:
            while x > 0:
                last_digit = x % 10
                reversed_number = reversed_number*10 + last_digit
                x //= 10 
            print(reversed_number)
        return original == reversed_number

