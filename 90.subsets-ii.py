class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(curr_list, curr_res, res):
            if curr_list == []:
                return
            for i in range(len(curr_list)):
                if curr_res+[curr_list[i]] not in res:
                    res.append(curr_res+[curr_list[i]])
                    dfs(curr_list[i+1:], curr_res+[curr_list[i]], res)

        nums.sort()
        res = []
        dfs(nums, [], res)
        res.append([])
        return res

        