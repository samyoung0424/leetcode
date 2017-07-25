class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        while left <= right:
            mid = (left+right)/2
            if mid**2 <= x and (mid+1) ** 2 > x:
                break
            elif mid**2 < x:
                left  = mid + 1
            elif mid ** 2 > x:
                right = mid - 1

        return mid