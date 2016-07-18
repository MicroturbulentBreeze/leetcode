class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = ListNode(0)
        res= head
        while l1 is not None:
            if l2 is None:
                head.next = l1
                return res.next
            elif l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else :
                head.next = l2
                l2=l2.next
            head=head.next
        if l2 is not None:
            head.next = l2
        return res.next
    def mergeKListsa(self, lists,l,r):
        if l > r:
            return None
        if l == r:
            return lists[l]
        if l + 1 == r :
            return self.mergeTwoLists(lists[l], lists[r])
        m = l+(r-l)/2
        return self.mergeTwoLists(self.mergeKListsa(lists,l,m), self.mergeKListsa(lists,m+1,r))
        
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return self.mergeKListsa(lists,0,len(lists)-1)
        