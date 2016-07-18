# -*- coding : utf-8 -*-
new_s="cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
s = "aabaaaa"
new_s= '$#%s#$'%"#".join(s)

l,right_i,right_position,max_i,max_length = len(new_s),1,1,1,1
p= [0]*l
for i in range(1,l-1):
	p[i] =1 if i>right_position else min(p[right_i*2-i],right_position-i)
	while new_s[i+p[i]]==new_s[i-p[i]] and new_s[i+p[i]]!='$' and new_s[i-p[i]]!='$' : 
		p[i]+=1
	if i+p[i] > right_position:		
		right_position = i+p[i]
		right_i = i		
		if max_length < p[i] :
			max_length = p[i]
			max_i = i		
		if i + p [i]  >= l-1:
			break
l_i = (max_i - max_length )/2
return s[l_i:l_i+max_length -1]