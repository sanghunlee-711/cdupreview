"""
a = list(map(int,input().split()))
for i in range(len(a)):
    if a[i] > 100:
        print('잘못된 점수')

average = sum(a)/4
if average >= 80:
    print('합격')
else:
    print('불합격')
"""
"""# if 조건문 응용
a,b,c,d = map(int, input().split())
average = (a+b+c+d)/4
if 0 <= a <=100 and 0 <= b <=100 and 0 <= c <=100 and 0 <= d <=100:
    if average >= 80:
        print("합격")
    else:
        print("불합격")
else:
    print("잘못된 점수")

age = int(input())
balance = 9000
if 7 <= age  <=12:
    balance -= 650
elif 13 <= age <= 18:
    balance -= 1050
elif age >= 19:
    balance -= 1250 
print(balance)


a = int(input())
for i in range(1,10,1):
    print("{} * {} = {}".format(a,i,a*i))

count = int(input('반복할 횟수를 입력하세용: '))

i = 0
while i < count:
    print('HelloWorld', i)
    i+=1

import random

print(random.random())

print(random.randint(1,6))

i = 0
while i != 3:
    i = random.randint(1,6)
    print(i)
# 이렇게 while은 반복횟수가 정해져 있지 않을때 유용하다.

dice = [1,2,3,4,5,6]
while i != 6:
    i = random.choice(dice)
    print(i)
"""
#1350won/1try while문 응용
"""
a = int(input())
while a >= 0:
    a -= 1350
    if a < 0:
        break
    else:
        print(a)

amount = int(input())
while amount >= 1350:
    amount -= 1350
    print(amount)
"""
"""
#continue문 응용
for i in range(100):
    if i % 2 ==0:
        continue # if 조건이 true이면  아래의 print(i)를 뛰어넘고 다시 진행됨.
    print(i)

"""
"""
#원하는 만큼 반복시키는 방법
#while 문 이용
count = int(input('반복할 횟수를 입력: '))

i = 0
while True:
    print(i)
    i += 1
    if i == count:
        break
#for 문 이용

for i in range(count +1):
    if i == count:
        break
    else:
        print(i)
"""
start, stop = map(int, input().split())

i = start

while True:
    if i % 10 == 3:
        i+=1
        continue
    if i > stop:
        break
        print(i, end = ' ')
        i += 1

