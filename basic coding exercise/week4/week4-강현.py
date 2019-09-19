# 4장

# Q1
def is_odd(num) :
    return True if num%2 == 1 else False

# Q2
def mean(*args) :
    return sum(args)/len(args)

# Q3
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %d 입니다" % total)

# Q5
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

# Q6
f = open('test.txt', 'a+')
f.write(input())
f.write('\n')
f.close()

# Q7
f = open('test.txt', 'r+')
text = f.read()
pos = text.find('java')
f.seek(pos+1)
f.write('python')
f.write(text[pos+4:])
f.close()


# 5장

# Q1
class Calculator :
    def __init__(self) :
        self.value = 0

    def add(self, val) :
        self.value += val

class UpgradeCalculator(Calculator) :
    def minus(self, val) :
        self.value -= val

# Q2
class MaxLimitCalculator(Calculator) :
    def add(self, val) :
        self.value = self.value + val if self.value + val < 100 else 100

# Q4
list(filter(lambda x : x >= 0, [1, -2, 3, -5, 8, -3]))

# Q5
int('0xea', 16)

# Q6
list(map(lambda x : 3*x, [1, 2, 3, 4]))

# Q7
max([-8, 2, 7, 5, -3, 5, 0, 1]) + min([-8, 2, 7, 5, -3, 5, 0, 1])

# Q8
round(17/3, 4)

# Q9
from sys import argv
try :
    print(sum(list(map(int, argv[1:]))))
except :
    pass

# Q10
import os
os.chdir("C:\doit")
print(os.popen("dir").read())

# Q11
from glob import glob
glob("c:/doit/*.py")

# Q12
import time
time.strftime('%Y/%m/%d/ %X', time.localtime(time.time()))

# Q13
from random import choice
pick = []
number = list(range(1,46))
for i in range(6) :
    pick.append(number.pop(number.index(choice(number))))
print(pick)
