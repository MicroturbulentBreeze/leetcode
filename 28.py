class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def get_next(s):
        	k=0
        	l=len(s)
        	next=[0]*l
        	for i in range(1,l):
        		while k>0 and s[i]!=s[k]:
        			k=next[k-1]
        		if s[i] == s[k]:
        			k=k+1
        		next[i] = k
        	return next
        	
        if needle == "":
        	return 0
        next = get_next(needle)
        l1,l2,i,k=len(haystack),len(needle),0,0
        while i < l1:
        	while k>0 and  haystack[i] != needle[k]:
        		k=next[k-1]
        	if haystack[i] == needle[k]:
        	    k=k+1
        	if k==l2:
        	    return i-l2+1
        	i=i+1
        return -1