"""



先看当前点属于那个窗口，如果都不属于，就输出IGNORED
如果属于某一个，很简单，最上面的置于顶层


done ok
"""


n,m=list(map(int,input().strip().split()))
martrix=[]
points=[]
for i in range(n):
	martrix.append(list(map(int,input().strip().split())))

for j in range(m):
	points.append(list(map(int,input().strip().split())))

getIndex=martrix[::]

def inMartix(lst,pointXY):
	x1,y1,x2,y2=lst
	x,y=pointXY
	if x1<=x<=x2 and y1<=y<=y2:
		return True
	else:
		return False

for pt in points:
	found=False
	for mt in martrix[::-1]:
		if inMartix(mt,pt):
			temp=mt
			# change layer
			print(getIndex.index(temp)+1)
			martrix.remove(temp)
			martrix.append(temp)
			found=True
			break
	if not found:
		print("IGNORED")


