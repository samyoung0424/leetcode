class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        path_block = path.split('/')
        for item in path_block:
            if item == '..':
                if len(stack) != 0:
                    stack.pop()
                else:
                    continue
            elif item == '.' or item == '':
                continue
            else:
                stack.append(item)

        res = '/' + '/'.join(stack)
        return res
