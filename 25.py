class Solution(object):
    def enough_nodes(self, head, k,node):
        s,l = head,k
        while s and l:
            s=s.next
            l-=1
        if l==0:
            node = s
            return True
        return False
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node = None
        res = ListNode(0)
        temp = res
        while self.enough_nodes(head,k,node):
            for i in range(k):
    
                temp = temp.next
            head = node_list[k]
            node_list = []
        if node_list == []:
            temp.next = None
        else:
            temp.next = node_list[0]
        
        return res.next