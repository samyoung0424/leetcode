class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[1 for i in range(n)] for i in range(n)]
        s = 1
        left, right, top, bottom = 0, n-1, 0, n-1
        while left <= right and top <= bottom:
            for j in range(left, right+1):
                res[top][j] = s
                s += 1
            top += 1
            for i in range(top, bottom+1):
                res[i][right] = s
                s += 1
            right -= 1
            for j in reversed(range(left, right+1)):
                res[bottom][j] = s
                s += 1
            bottom -= 1
            for i in reversed(range(top, bottom+1)):
                res[i][left] = s
                s += 1
            left += 1

        return res



