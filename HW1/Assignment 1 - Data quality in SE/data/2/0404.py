T=int(input())
for _ in range(0,T):
	s=input()
	val=len(s)//2
	if len(s)%2==1:
		str1=s[:val]
		str2=s[(val+1):]
	else:
		str1=s[:val]
		str2=s[(val):]
	d={}
	d1={}
	for i in str1:
		d[i]=str1.count(i)
	for i in str2:
		d1[i]=str2.count(i)
	l1=list(d.values())
	l2=list(d1.values())
	l3=list(d.keys())
	l4=list(d1.keys())
	flag=0
	for i in str1:
		if i in str2:
			if d[i]!=d1[i]:
				flag=1
				print("NO")
				break
		else:
			print("NO")
			flag=1
			break
	if flag==0:
		print("YES")
	
		
