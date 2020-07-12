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


for i in range(5):
    for j in range(5):
        print('j:', j, sep = '', end = ' ')
    
    print('i:', i, '\\n', sep = '')    
#출력
j:0 j:1 j:2 j:3 j:4 i:0\n
j:0 j:1 j:2 j:3 j:4 i:1\n
j:0 j:1 j:2 j:3 j:4 i:2\n
j:0 j:1 j:2 j:3 j:4 i:3\n
j:0 j:1 j:2 j:3 j:4 i:4\n


for i in range(5): # 5번 반복. 바깥쪽 루프 세로방향
    for j in range(5): # 5번반복 안쪽루프 가로방향
        print('*', end = '') # 줄바꿈 방지 위한 end
    print() #가로방향으로 다 그린 뒤 다음줄로 넘어가기 위함.

for i in range(5): #vertical
    for j in range(5): # horizontal
        if j <= i:
            print('*', end = '')
    print() # for next line


for i in range(5):
    for j in range(5):
        if i == j:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()

for i in range(5):
    for j in range(5):
        if j < i:
            print(' ', end = "")
        else:
            print('*', end = '')



n = int(input())

for i in range(1,n+1):
    print(' '*(n-i), '*'*(2*i-1))   


n = int(input())

for i in range(n):
    for j in reversed(range(n)):
        if j > i:
            print(' ', end = "")
        else:
            print('*', end = "")
    for j in range(n):
        if j < i:
            print('*', end ="")
    print()

a, b = map(int, input().split())

for i in range(a,b+1,1):  i % 5 ==0 and i % 7 ==0 
    if i % 5 ==0:
        print('Fizz')
    elif i & 7 ==0:
        print('Buzz')
    elif :
        print('FizzBuzz')
    else:
        print(i)
"""
"""
import turtle as t

n = int(input())
t.shape('turtle')
for i in range(n): # 5각형이니 5번 반복
    t.forward(100)
    t.right(360/n) # 360을 5 로나누어 외각 구하기
t.mainloop()

#즉, 공통된 부분을 일반화해서 원하는 결과를 얻어내는 과정이 프로그래밍이며 컴퓨테이셔널 씽킹입니다.

import turtle as t

n = int(input())
t.shape('turtle')
t.color('red') #펜의 색 빨간색으로 지정
t.begin_fill()#색칠할 영역 시작
for i in range(n):
    t.forward(100)
    t.right(360 / n)
t.end_fill()
t.mainloop()

import turtle as t
t.shape('turtle')
t.circle(120) # 반지름 120인 원
t.mainloop()


import turtle as t

n = 60
t.shape('turtle')
t.speed('fastest') #거북이속도를 가장 빠르게 설정(0.5부터 10까지 설정가능)
for i in range(n):
    t.circle(120) 
    t.right(360/n) #오른쪽으로 360/n도 회전 

import turtle as t

t.shape('circle')
t.speed('fastest')
for i in range(300):
    t.forward(i) # i만큼 앞으로 이동. 300번 만큼 길어지는것임
    t.right(91) # 오른쪽으로 91도 회전
t.mainloop()

import turtle as t

n = 5
t.shape('turtle')
for i in range(n):
    t.forward(100)
    t.right((360/n)*2)
    t.forward(100)
    t.left(360/n)
t.mainloop()


import turtle as t

n, line = map(int,input().split())
t.shape('turtle')
t.speed('fastest')

for i in range(n):
    t.forward(line)
    t.right((360/n)*2)
    t.forward(line)
    t.left(360/n)
t.mainloop()

a = [10,20,30]
a.remove(20)
print(a)
print(len(a))

from collections import deque
a = deque([10,20,30])
print(deque)
a.append(500)
a.popleft()

a, b = map(int, input().split())
c = [2**i for i in range(a,b+1)]
del c[1] # del과 pop은 index요소로 삭제가능하나 remove는 값으로 삭제가능함.
del c[-2]
print(c)

a = [[10,20],[30,40],[50,60]]
from pprint import pprint
pprint(a, indent = 4, width= 20) #사각형 모양으로 이중리스트 출력원할시
    [ [10,20],
    [30,40],
    [50,60]]

a = [[10,20],[30,40],[50,60]]
for x,y in a:
    print(x,y)
print()

for i in a: #전체리스트에서 가로 한줄씩 
    for j in i: #가로한줄안에서 가로 안쪽 요소꺼냄
        print(j, end = ' ')
    print()
print()

for i in range(len(a)): #len(a) 는 3 으로 세로크기
    for j in range(len(a[i])): #len(a[i])는 2로 가로크기
        print(a[i][j], end = ' ')
    print()
print()

i = 0
while i < len(a):
    x, y = a[i]
    print(x,y)
    i +=1

print()
i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end = ' ')
        j += 1
    print()
    i += 1

print("반복문으로 1차원 리스트 만들기")
a = []
for i in range(10):
    a.append(0) # append로 요소 추가
print(a)

print("반복문으로 2 차원 리스트만들기[append이용]")

a = []
for i in range(3):
    line =[] #안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(2):
        line.append(0) #안쪽리스트에 0 추가
    a.append(line) #전체리스트에 안쪽리스트 추가
print(a)

print('리스트 표현식으로 2 차원 list만들기')

a = [[0 for j in range(2)]for i in range(3)]
print(a)

print('리스트자체 곱을 통한 2 차원 list만들기')
a = [[0]*2 for i in range(3)]
print(a)

print('톱니형리스트 만들기(가로크기지정)')
a = [3,1,3,2,5]#
b =[]
for i in a:
    line =[]
    for j in range(i):
        line.append(0)
    b.append(line)
print(b)

print('톱니형 리스트 만들기(표현식)')
a = [[0]*i for i in [3,1,3,2,5]]
print(a)

print('sorted 로 2 차원 리스트정렬')
students = [['jhon', 'C', 19],
            ['maria','A',25],
            ['andrew','B',7]]
print(sorted(students, key = lambda student :student[1]))
#안쪽리스트 인덱스 1을 기준
print(sorted(students, key = lambda student :student[2]))
#안쪽리스트의 인덱스 2를 기준

print('리스트 할당')
a = [[10,20], [30,40]]
b = a
b[0][0] = 500
print(a)
print(b) #이렇게 할당을 하면 두개의 값이 모두 바뀜

print('copy')

a =[[30,50],[60,80]]
b = a.copy()
b[0][0] =6060
print(a)
print(b)

print('decopy')

a = [[90,34],[70,40]]
import copy
b = copy.deepcopy(a)
b[0][0] =700
print(a)
print(b)


print('practice:3차원리스트만들기')

a = [[[0for i in range(3)]for j in range(4)]for k in range(2)]
# 높이 세로 가로 크기로 3차원 리스트 생성된다.
a = [[[0for column in range(3)]for row in range(4)]for depth in range(2)]
print(a)


a = [3,1,3,2,5]#
b =[]
for i in a:
    line =[]
    for j in range(i):
        line.append(0)
    b.append(line)
print(b)

#다시풀어보기 : https://dojang.io/mod/quiz/summary.php?attempt=1003382&cmid=2298
col, row =map(int,input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))
    for j in range(col):
        matrix[i].append(list(input()))
    matrix.append(matrix[i])

print(matrix)

a = 'Hello, world!'
a = a.replace('world!', 'Python')
print(a)

table = str.maketrans('aeiou', '12345') #문자열 안의 다른문자 바꿈 , 바꿀문자 , 새문자
'apple'.translate(table)
print(table)


a = 'python'
a = a.rjust(10)
print(a)

b = 'python2'
b = b.upper().rjust(30)
print(b)

# zerofill(보통 자릿수를 맞추기 위해 사용)
c = '35'
c = c.zfill(4)
print(c)

#문자열 위치 찾기
#오른쪽에서 부터 찾을때는 rfind 값이 존재하지 않을때는 index값이 뜨지 않고 -1 이 반환됨.
d = 'apple pineapple'.rfind('pl')
print(d)


#포맷팅(문자열서식지정등)
print('Hello, {0}'.format('world!'))
print("Hello, {0} {2} {1}".format('Python', "script", 3.6))
#brace안에 있는 숫자는 들어갈 인덱스를 지정하는것
#output ->Hello, Python 3.6 script

print('{0} {0} {1} {1}'.format('mef', 2323))

language = "Python"
version = 3.8
print(f'Hello, {language},{version}')

#format 으로 문자열정렬하기
print('{0:<10}'.format('python'))#'{인덱스:<길이}'.format값
print('{0:>10}'.format('python'))

#foramtting으로 숫자갯수 맞추기
print('%03d'%1) # %0개수 d  % 숫자
print('{0:03d}'.format(35)) # 인덱스:0 개수 d
print('%08.2f' %3.6) #소수점 이하 갯수까지 포함해 8개가됨
print('{0:08.2f}'.format(150.37))
print('{0:0<10}'.format(15)) #'{인덱스:[[채우기]정렬][길이][.자릿수][자료형]}'
print('{0:0>10}'.format(15)) #길이 10 오른쪽 정렬 남은공간 0으로 채움
print('{0: >10}'.format(15)) # 남는공간 공백으로 채움.
print('{0:x>10}'.format(15)) #남는공간 x로 채우고 오른쪽 정렬
#천단위 콤마넣기
print(format(10000000,','))

#파일경로에서 파일명만 가져오기
path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
x = path.split('\\')
filename = x[-1]
print(filename)

#python.exe

filename = path[path.rfine('\\')+1:]
#파일명은 항상 마지막에 있으므로 rfind를 사용해서 오른쪽에서 부터의 \\를 찾는것.
#\\ 다음이 파일명일 테니 +1 해주는것

paragraph = input()
words = list(paragraph.split())
count = 0
for i in words:
    i.strip(',.')
    if i == 'the':
        count += 1
print(count)

a = list(map(int, input().split(';')))
b = sorted(a, reverse=True)
for i in b:
    print('{0: >9,}'.format(i))

#처음에는 아래와 같이 작성했는데 sort를 사용하면 Nontype으로 생겨버린다.
#문제는 각자 type을 한번 찾아봐야할 것 같음 그래서 그냥 sorted씀
a = list(map(int, input().split(';')))
b = a.sort(reverse=True)
for i in b:
    print('{0: >9,}'.format(i))


print('dictionary 키 쌍 값 추가하기')
#setdefault:키-값 쌍 추가
#update: 키의 값 수정, 키가 없으면 키 쌍 값 추가
x = {'a':10,'b':20,'c':30,'d':40}
x.setdefault('e')
x.setdefault('f',100)
print(x)
x.update(a=100)
print(x)
x.update(g= 800)
print(x)
x.update(a=900, h = 324)
print(x)

#update는 키가 문자열일때만 사용가능함. 숫자일경우 딕셔너리를 이용해야함
y = {1: 'one', 2:'two'}
print(y)
y.update({1:'ONE', 3:'Three'})
print(y)
y.update([[2,'Two'], [4,"FOUR"]]) #리스트와 튜플을 이용하여 딕셔너리에 값추가
print(y)
y.update(zip([1,2], ['one','two'])) # zip을 이용하여 수정
print(y)
#setdefault는 키 값의 쌍만 추가할 수 있으며 이미 들어 있는 값을 바꾸려해도 안 바꿔짐

x = {'a':10, 'b':20, 'c':30, 'd':40}
x.pop('a') #a의 key&value를 제거함.
print(x)

x = {'a':10, 'b':20, 'c':30, 'd':40}
del x['a'] #a의 key&value를 제거함.
print(x)

x ={'a':10, 'b':20,'c':30,'d':40}
x.popitem() #오른쪽끝의 키값인 d:40 부터 제거된다.
print(x)

x ={'a':10, 'b':20,'c':30,'d':40}
x.clear()
print(x)

x ={'a':10, 'b':20,'c':30,'d':40}
print(x.get('a')) #해당 key값 미존재시 0으로 값 반환

#items: 키-값 쌍을 모두 가져옴
#keys: 키를 모두 가져옴
#values: 값을 모두 가져옴
print(x.items())
print(x.keys())
print(x.values())

print('list로 dict만들기')
keys = ['a','b','c','d']
x = dict.fromkeys(keys) #키리스트로 딕셔너리를 만들어 값은 모두 none으로 저장함.
print(x)
y = dict.fromkeys(keys,100)
print(y) #이렇게 값지정하면 값 다들어감 일정하게

#키가 존재하지 않을때 오류방지하는방법
from collections import defaultdict
y = defaultdict(int)
print(y['z']) #이렇게하면 존재하지 않는 key일때 오류발생이아닌 0이 출력된다.

x ={'a':10, 'b':20, 'c':30, 'd':40}
for i in x:
    print(i, end = ' ')

print()

for i,j in x.items():
    print(i,j)
print()
for key in x.keys():
    print(key, end = ' ')

print()

for values in x.values():
    print(values, end = ' ')

print('반복문을 이용한 dict 생성하기')
print('{키: 값 for 키, 값 in 딕셔너리}')
print("dict({키: 값 for 키, 값 in 딕셔너리})")
keys = ['a','b','c','d']
x = {key:value for key, value in dict.fromkeys(keys).items()}
print(x)

keys = ['a','b','c','d']
x = {key: 0 for key in dict.fromkeys(['a','b','c','d']).keys()}
print(x)

a = {'a':10, 'b':20, 'c':30, 'd':40}
x = {key: 0 for key in dict.fromkeys(a).keys()}
y = {value: 0 for value in a.values()}
print(x) # key를 value가 0인 dict로 가져와서 프린트
print(y) # value값이 key 이며 새로운 Value가 0인것인 dict로 프린트
z = {value: key for key, value in a.items()}
print(z) #key value 위치 바꿔서 출력

x = {'a':10, 'b':20, 'c':30, 'd':40}

for key, value in x.items():
    if value == 20:
        del x[key]
print(x)
#이렇게 직접 삭제할 수가 없음 도중에 dict의 크기가 바뀌었다는 Error가 뜨기 때문

x = {key: value for key, value in x.items()if value != 20}
print(x)



maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science':83}
average = sum(maria.values())/len(maria)
print(average)


keys = input().split()
values = map(int, input().split())

x = dict(zip(keys,values))
del x['delta']
x = {key: value for key, value in x.items()if value !=30}
print(x)
#set 에 대해알아보장
a = set('apple')
print(a) #반복되는것은 사라지고 set이 생성됨
#print(a['l']) # 이렇게 따로 대괄호로 불러내지 못함.
b =set(range(5))
print(b)
c =set()
print(c)

a ={1,2,3,4}
b ={3,4,5,6}
print(a|b)
print(set.union(a,b))
#set.union() 또는 or연산자로 합집합(union)을 구할 수 있다.
print(a&b)
print(set.intersection(a,b))
#set.intersection() 또는 and연산자로 교집합(intersection)을 구할 수 있다.
print(a-b)
print(set.difference(a,b))
# 차집합(difference)를 구하는 방법
print(a ^ b)
print(set.symmetric_difference(a,b))
#대칭차집합(symmetric difference)를 구하는 방법.

a = {1,2,3,4}
a|={5}# |= 연산자를 통하여 update메소드와 동일하게 집합내 요소를 추가할 수 있다.
a.update({6})
print(a) 
a &={0,1,2,3,4} # &=연산자를 통해 겹치는 요소만 세트에 저장할 수 있다.(intersection_update메소드와 같음)
print(a) 
a.intersection_update({3,4,5,6})
print(a)

a = {1,2,3,4,5}
a -= {3} #해당 원소제거해준다.
print(a)
a.difference_update({5})
print(a)

a = {1,2,3,4,5}
a ^={3,4,5,6} # 겹치지 않는요소만 출력해준다
#a.symmetric_difference_update({3,4,5,6}) #위와 동일

print(a)

#집합관계표시하기
a = {1,2,3,4}
print(a <= {1,2,3,4})
print(a.issubset({1,2,3,4,5})) #a 가 {1,2,3,4}의 부분집합인지 확인
print(a < {1,2,3,4,5}) # set a 가 {1,2,3,4,5}의 진 부분 집합인지 확인
print(a >= {1,2,3,4}) #a가 1,2,3,4의 상위집합인지 확인
print(a.issuperset({1,2,3,4})) #이하동문
print(a.isdisjoint({5,6,7,8})) #겹치는 요소가 없어서 true
print(a.isdisjoint({3,4,5,6})) #3,4 가 겹처서 False

a = {1,2,3,4}
a.add(5) # 세트에 요소추가
print(a) 
a.remove(3)
print(a) #세트에 요소 제거
a.discard(2)
a.discard(5)# 세트에 요소가 있으면 삭제 없으면 그냥 넘어감
print(a)
#pop,len은 list와 동일하게 사용됨.

#set생성하기
a = {i for i in 'apple'}
print(a) #중복된 친구들 제거됨
a = {i for i in'pineapple' if i not in'apl'}
print(a)

# 1~100까지 중 3과 5의 공배수를 세트형태로 출력하기
a ={i for i in range(1,101)if i%3 == 0}
b ={i for i in range(1,101)if i % 5 == 0}
print(a&b)
print(set.intersection(a,b))
"""
n, m = map(int, input().split())
a = {i for i in range(1,n+1,1) if n%i == 0}
b = {j for j in range(1,m+1,1) if m%j == 0}
print(a)
divisor = a & b

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)