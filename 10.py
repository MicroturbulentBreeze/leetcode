class Solution(object):
    def isMatch(self, a, b):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if b=="":
            return a==""
        m = len(a)
        n = len(b)
        print m,n
        d={}
        d[(-1,-1)] = True
        for j in range (m):
        	d[(-1,j)] = False
        for i in range (n):
        	for j in range (-1,m):
        
        		if j == -1:
        			if b[i] == '*' :
        				d[(i,j)] = d[(i-2,j)]
        			else :
        				d[(i,j)] = False
        		elif i == 0:
        			d[(i,j)] = (b[i] == a[j] or b[i] =='.') and (j==0 or d[(i-1,j-1)])
        		elif b[i] == '*':
        			d[(i,j)] = (i > 1 and d[(i-2,j)])  or  ((b[i-1]==a[j] or b[i-1] == '.') and (  d[(i-1,j-1)] or d[(i,j-1)] ) )
        		elif b[i] == a[j] or b[i] == '.':
        			d[(i,j)] =  d[(i-1,j-1)]
        		else:
        			d[(i,j)] = False 
        
        return d[(n-1,m-1)]
