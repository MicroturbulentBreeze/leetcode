# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        father = res
        
        while head and head.next:
            print head.val
            father.next = head.next
            temp = head.next.next
            father.next.next = head
            father = head
            head = temp
        father.next = head
        return res.next