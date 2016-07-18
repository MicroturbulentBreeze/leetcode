class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False
        if x < 0:
            flag = True
            x=-x
        a=[]
        while x > 0:
            a.append(x%10)
            x=x/10
        res = 0
        for i in a:
           res = res*10 + i
        if flag:
            res = -res
        if res > 2147483647 or res < -2147483648 :
            return 0
        return res