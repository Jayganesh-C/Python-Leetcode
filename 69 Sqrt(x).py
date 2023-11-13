class Solution:
    def mySqrt(self, x: int) -> int:
        if(x==0):
            return x
        first, last = 0, x
        while(first <= last):
            mid = first + (last-first)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                first = mid+1
            else:
                last = mid-1
        return last


