a="aaaaaaaaaaaaab"
b="a*a*a*a*a*a*a*a*a*a*c"
def is_match(s1,s2):
	if s1 == "":
		return s2==""
	if len(s1) == 1 :
		return len(s2)==1 and (s1[0]==s2[0] or s1[0]=='.')
	if s1[1] == '*' :
		return is_match(s1[2:],s2) or (len(s2)!=0 and (s1[0]==s2[0] or s1[0]=='.') and is_match(s1,s2[1:]))
	else :
		return s2 != "" and (s1[0]==s2[0] or s1[0]=='.') and is_match(s1[1:],s2[1:])
print is_match(b,a)