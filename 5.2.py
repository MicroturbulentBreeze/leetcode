class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s= '$#'+"#".join(s)+'#$'
    
        l, max_i, max_position, max_p_i = len(s),0 ,0 , 1
        p= [0]
        for i in range(1,l-1):
            if max_i > i :
            	p.append(min(p[max_i*2-i],max_position-i))
            else :
            	p.append(1)
            while s[i+p[i]]==s[i-p[i]] and s[i+p[i]]!='$' and s[i-p[i]]!='$' : 
            	p[i]+=1
            if i+p[i] > max_position:
            	max_position = i+p[i]
            	max_i = i
                if i + p [i]  >= l-1:
                    if p[max_p_i] < p[i]:
                        max_p_i = i
                    break
            if p[max_p_i] < p[i] :
                max_p_i = i
        s= s[max_p_i-p[max_p_i]+1:max_p_i+p[max_p_i]].split('#')
        return ''.join(s)     
        