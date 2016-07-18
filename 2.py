# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None :
            return l2
        if l2 is None :
            return l1
        l3=l1;

        c = 0
        father_l1 = l1
        father_l2 = l2
        while l1 is not None :
            val_l2 = 0
            if l2 is not None :
                val_l2 = l2.val
                l2 = l2.next
            val = l1.val + val_l2+ c
            c = val/10
            l1.val = val%10
            father_l1 = l1
            father_l2 = l1
            l1 = l1.next
        
        if l2 is not None :
            father_l1.next=l2
        
        while l2 is not None:
            if c ==0:
                break
            val = l2.val +c
            c = val/10
            l2.val = val%10
            father_l2 =l2
            l2=l2.next
        if c != 0:
            father_l2.next = ListNode(c)
                
        return l3
            