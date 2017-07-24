# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        start, end = head, head
        count = 1
        while end.next != None:
            end = end.next
            count += 1
        k %= count
        while k > 0 :
            end.next = start
            start = end
            new_end = head
            while new_end.next != end:
                new_end = new_end.next
            new_end.next = None
            end = new_end
            k -= 1

        return start

#
# if __name__ == '__main__':
#     input = [1,2,3,4,5]
#     nodelist = []
#     for item in input:
#         tmp_node = ListNode(item)
#         nodelist.append(tmp_node)
#     for i in range(len(nodelist)-1):
#         nodelist[i].next = nodelist[i+1]
#
#     # start = nodelist[0]
#     # while start != None:
#     #     print start.val
#     #     start = start.next
#
#     sol = Solution()
#     res = sol.rotateRight(nodelist[0], 2)
#     while res != None:
#         print res.val
#         res = res.next
