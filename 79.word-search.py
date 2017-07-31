class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(word, i, j, board):
            if len(word) == 0:
                return True
            if board[i][j] == word[0]:
                if len(board) == 1 and len(board[0]) == 1 and len(word) == 1:
                    return True
                tmp = board[i][j]
                board[i][j] = '#'
                if i!= 0:
                    top = dfs(word[1:], i-1, j, board)
                    if top:
                        return True
                else:
                    top = False
                if i!= len(board)-1:
                    bottom = dfs(word[1:], i+1, j, board)
                    if bottom:
                        return True
                else:
                    bottom = False
                if j!= 0:
                    left = dfs(word[1:], i, j-1, board)
                    if left:
                        return True
                else:
                    left = False
                if j!= len(board[0]) - 1:
                    right = dfs(word[1:], i, j+1, board)
                    if right:
                        return True
                else:
                    right = False

                board[i][j] = tmp
                return top or bottom or left or right
            else:
                return False


        if len(board) == 0:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(word, i, j, board):
                    return True
        return False


# if __name__ == '__main__':
#     sol = Solution()
#     board = [['c', 'a', 'a'], ['a', 'a', 'a'], ['b','c', 'd']]
#     word = 'aab'
#     print sol.exist(board, word)