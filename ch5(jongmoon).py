#5
#1.
>>> class UpgradeCalculator(Calculator):
	def minus(self, val):
		self.value = self.value-val

#2.
	def add(self, val):
		if self.value+val>100:
			return 100
		else:
			self.value+=val 
#왜 return self.vlaue+=val하면 안되나요

#3.
#(1) ?		=> 1, 2, 0은 반복인가?
#(2) True

#4.
>>> list(filter(lambda x: x > 0, [1,-2,3,-5,8,-3]))

#5. 
>>> int(0xea)

#6. 
>>> list(map(lambda a: a*3, [1,2,3,4]))

#7.
>>> max([-8, 2, 7, 5, -3, 5, 0, 1])+min([-8, 2, 7, 5, -3, 5, 0, 1])

#8.
>>> round(17/3, 4)

#9.
#모르겠어요. 흑흑흑

#10.
>>> import os
>>> os.chdir("C:\doit")
>>> a=os.system("dir")
>>> print(a)

#11.
>>> glob.glob("C:/doit/*py")


#12.
>>>time.strftime('%Y/%m%d %X')

#13.
import random
def random_pop(data):
    number=random.randint(0, len(data)-1)
    return data.pop(number)

if __name__=='__main__':
    data = list(range(1,45))
    while data:
        print(random_pop(data))
#이거로 저장을 한 뒤에...흠... 6개의 숫자가 튀어져 나오려면 6번을 시행해야 하는건지. 아니면 동시에 random하게 45개 중 6개가 나오는 것인지.
