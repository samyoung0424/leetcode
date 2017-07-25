class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for i in range(m)]
        sum = 0
        for i in range(m):
            sum += grid[i][0]
            dp[i][0] = sum
        sum = 0
        for j in range(n):
            sum += grid[0][j]
            dp[0][j] = sum

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
            