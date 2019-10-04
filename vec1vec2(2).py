#1번
>>> def add(vec1, vec2):
	x=[]
	for i in range(0,len(vec1)-1):
		x.append(vec1[i]+vec2[i])
		return list(x)
#after feedback
>>> def add(vec1, vec2):
	x=[]
	for i in range(len(vec1)):
		x.append(vec1[i]+vec2[i])
	return list(x)
#여기서 x가 list였기 때문에 list안 써도 되고, range함수의 범위 잘 보고. 나의 처음 가장 큰 문제점은 return구문의 위치였음.



>>> def add1(vec1, vec2)
    return [val + vec2[i] for i, val in enumerate(vec1)]
#여기서 i는 index임. enumerate을 써서.
>>> for i, val in enumerate['a','c','x']
#이거 for문에 i와 val이 모두 돌아가는 것임.

#2번
>>> def multiply(scal, vec):
	x=[]
	for i in range(len(vec)):
		x.append(vec[i]*scal)
	return x
    
