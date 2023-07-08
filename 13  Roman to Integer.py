class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        previous_val = 1001
        sum = 0
        for st in s:
            curr_val = roman_dict[st]
            if previous_val < curr_val:
                sum += curr_val - (previous_val * 2)
            else:
                sum += curr_val
            previous_val = curr_val
        return sum
