class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.is_match(s,p)
    def is_match(self,s,p):
    	ls,lp,s0,p0,i,j = len(s),len(p),0,-1,0,0
    	while i < ls:
    		if j<lp and (p[j]=="?" or s[i] == p[j]):
    			i+=1
    			j+=1
    			continue
    		elif j<lp and p[j]=='*':
    			p0 = j
    			j+=1
    			s0 = i
    			continue
    		elif p0 >= 0:
    			s0+=1
    			i=s0
    			j=p0+1
    			continue
    		else:
    			return False
    	while j<lp and p[j]=="*":
    		j+=1
    	if j != lp:
    		return False
    	return True