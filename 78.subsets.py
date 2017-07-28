class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(curr_list, curr_sol, res):
            if curr_list == []:
                return
            for i in range(len(curr_list)):
                res.append(curr_sol+[curr_list[i]])
                dfs(curr_list[i+1:], curr_sol + [curr_list[i]], res)

        res = []
        dfs(nums, [], res)
        res.append([])
        return res