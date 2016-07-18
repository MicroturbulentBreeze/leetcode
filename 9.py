import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        l = int(math.log(x+0.01)//math.log(10))+1
        a = 10 ** (l-1)
        b = 10

        for i in range((l//2)):
        	if x/a%10 ==x%b*10//b :
        		a/=10
        		b*=10
        	else :
        		return False
        return True
        