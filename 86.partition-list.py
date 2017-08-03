# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        end = head
        l = 0
        while end.next:
            end = end.next
            l += 1
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        count = 0
        while p.next and count <= l:
            if p.next.val < x:
                p = p.next
            else:
                end.next = p.next
                p.next = p.next.next
                end = end.next
                end.next = None
            count += 1

        return dummy.next
        