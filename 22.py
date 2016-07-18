class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        
        def get_list(l,a,n,sum):
        	if l == n:
        		a.append(n-sum)
        		s=""
        		for i in a:
        			s+= "("+")"*i
        		res.append(s)
        		a.pop()
        		return
        	for i in range(l-sum+1):
        		a.append(i)	
        		get_list(l+1,a,n,sum+i)
        		a.pop()
        get_list(1,[],n,0)
        return res


