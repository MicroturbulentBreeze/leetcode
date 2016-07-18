# -*- coding : utf-8 -*-
s="abcbefg"
s0 = s[::-1]
print s,s0
l = len(s)
d={}
index = 0
length = 0
for i in range(l):
	for j in range (l):
		print s[i],s0[j],
		if s[i]==s0[j]:
			if i*j==0:
				d[(i,j)] = 1
			else:
				d[(i,j)] = d[(i-1,j-1)] +1
			if d[(i,j)] >length :
				index = i
				length=d[(i,j)]
		else:			
			d[(i,j)] = 0
		print d[(i,j)],
	print 
print index ,length
print s[index-length+1 : index+1]