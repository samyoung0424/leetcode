class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(curr_list, curr_sol, res, k):
            if k == 0:
                res.append(curr_sol)
                return
            elif curr_list == []:
                return
            for i in range(len(curr_list)-k+1):
                dfs(curr_list[i+1:], curr_sol+[curr_list[i]], res, k-1)
        startlist = range(1, n+1)
        res = []
        dfs(startlist, [], res, k)
        return res