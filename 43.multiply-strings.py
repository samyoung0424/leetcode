class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        btoi = {
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9
        }
        itob = {
            0:'0',
            1:'1',
            2:'2',
            3:'3',
            4:'4',
            5:'5',
            6:'6',
            7:'7',
            8:'8',
            9:'9'
        }
        n_1, n_2 = 0, 0
        for i in range(-1, -len(num1)-1, -1):
            n_1 += btoi[num1[i]] * (10 ** (-(i+1)))
        for i in range(-1, -len(num2)-1, -1):
            n_2 += btoi[num2[i]] * (10 ** (-(i+1)))
        # print n_1, n_2
        prod = n_1*n_2
        if prod == 0:
            return '0'
        from collections import deque
        res = deque()
        while prod != 0:
            # print prod
            dig = prod % 10
            res.appendleft(itob[dig])
            prod /= 10
        res_str = ''.join(res)
        return res_str

# if __name__ == '__main__':
#     sol = Solution()
#     num1, num2 = '9', '99'
#     print sol.multiply(num1, num2)