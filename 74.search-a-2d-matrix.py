class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False
        # m = len(matrix)-1
        if matrix[0] == []:
            return False
        # n = len(matrix[0]) - 1
        #
        # top, bottom = 0, m
        # while top < bottom:
        #     v_mid = (top + bottom) / 2 + 1
        #     if matrix[v_mid][0] > target:
        #         bottom = v_mid-1
        #     elif matrix[v_mid][0] == target:
        #         bottom = v_mid
        #         break
        #     elif v_mid == top:
        #         bottom = top
        #     else:
        #         top = v_mid
        #
        #
        # left, right = 0, n
        # while left <= right:
        #     h_mid = (left + right) / 2
        #     if matrix[bottom][h_mid] > target:
        #         right = h_mid - 1
        #     elif matrix[bottom][h_mid] < target:
        #         left = h_mid + 1
        #     else:
        #         return True
        # return False
        i = 0
        j = len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False