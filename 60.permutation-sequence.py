class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        dig_list = range(1, n+1)
        import math
        res = []
        left = k-1
        while n > 0:
            n-=1
            digit, left = divmod(left, math.factorial(n))
            res.append(str(dig_list[digit]))
            dig_list.pop(digit)
        return ''.join(res)

# if __name__ == '__main__':
#     sol = Solution()
#     n = 4
#     k = 16
#     print sol.getPermutation(n, k)