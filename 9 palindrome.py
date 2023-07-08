class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Checks some edge cases, and returns False immediately if the number is negative or ends with a 0 (with the exception of the number 0 itself)
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        half = 0
        while x > half:
            half = (half * 10) + (x % 10)
            x = x // 10
        
        return x == half or x == half // 10