class Solution(object):
    res = ["1"]
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < len(self.res):
            return self.res[n-1]
        n -=len(self.res)
        res0= self.res[-1]
        while n > 0:
        	i = 0
        	ans = ""
        	l = len(res0)
        	for j in range(1,l+1):
        		#print i,j,ans
        		if j == l:
        			ans += str(j-i)+res0[j-1]
        		elif res0[j]!=res0[j-1]:
        			ans += str(j-i)+res0[j-1]
        			i = j
        	res0 = ans
        	self.res.append(ans)
        	n-=1    
        return self.res[n-1]
if __name__ == '__main__':
	print Solution().countAndSay(5)