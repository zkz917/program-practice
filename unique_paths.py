class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
        	dp[m][0] = 1
        for i in range(n):
        	dp[0][n] = 1

        for i in range(1,m):
        	for j in range(1,n):
        		dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[m-1][n-1]


