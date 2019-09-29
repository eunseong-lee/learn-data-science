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
