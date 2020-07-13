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
####
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

n, m = map(int, input().split())
a = {i for i in range(1,n+1,1) if n%i == 0}
b = {j for j in range(1,m+1,1) if m%j == 0}
print(a)
divisor = a & b

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)

#파이썬으로 파일을 생성하고 문자열 넣기
file = open('hello.txt','w') #hello.txt파일을 쓰기모드로(w)열기,w는 write의 쓰다이다.
file.write('Hello, world!') #파일객체를 얻었으니 내용바꿔줌
file.close() #파일객체 닫기

#문자열 읽기
file = open('hello.txt','r') #hello.txt파일을 읽기모드(read)로 열기. 파일객체 반환
s=file.read() #파일에서 문자열 읽기
print(s) #Hello,world!
file.close() #파일객체닫기

#매번 close로 닫으면 귀찮으니 with as 사용하여 자동으로 파일객체 닫기// with as 사용하면 파일을 사용한뒤 자동으로 파일객체를 닫아준다.
with open('hello.txt', 'r')as file: #hello.txt파일을 읽기모드(r)로 열기
    s = file.read() # 파일에서 문자열 읽기
    print(s) # Hello,world!

#문자열 여러줄을 파일에 넣기
with open('hello.txt', 'w')as file:
    for i in range(3):
        file.write("Hello, world! {0}\n".format(i))

#리스트에 들어있는 문자열을 파일에 써넣기

lines = ['안녕하세요.\n', '파이썬\n', '코딩도장입니다.\n']

with open('hello.txt', 'w')as file:
    file.writelines(lines)

#파일의 내용을 한줄씩 리스트로 가져오기 ( read는 내용을 읽어 문자열로 가져오지만 readlines는 파일의 내용을 한줄 씩 리스트 형태로 가져온다)
with open('hello.txt','r')as file:
    lines = file.readlines()
    print(line)

#파일의 내용을 한줄 씩 읽기
with open('hello.txt', 'r')as file:
    line = None  #line != ''와 충돌하지 않게 하기위해 None으로 미리 변수선언
    while line != '': #빈문자열이면 멈춤 문자열이 존재하면 계속 반복
        line = file.readline() #문자열 한줄씩 읽어서 변수에 저장
        print(line.strip('\n'))
# readline에서는 while을 쓰는것이 좋은데 파일에 문자열이 몇줄이나 있는지 모르기 때문이다.  

#for 반복문으로 파일의 내용을 줄단위로 읽기
with open('hello.txt', 'r')as file: #hello.txt파일을 읽기모드(r)로 열기
    for line in file: #for에 파일객체를 지정하면 파일의 내용을 한줄씩 읽어서 변수에 저장함
        print(line.strip('\n')) #파일에서 읽어온 문자열에서 \n 삭제하여 출력

#파일객체는 이터레이터라 변수여러개에 저장하는 언패킹도 가능하다
file = open('hello.txt', 'r')
a,b,c =  file
print(a,b,c) #이때 할당변수의 개수와 파일에 저장된 문자열의 줄 수가 일치해야한다.

#파이썬은 객체를 파일에 저장하는 pickle 모듈을 제공한다.
#객체를 파일에 저장하는것을 pickling, 파일에서 객체를 읽어오는 과정을 unpickling이라고 한다.
import pickle

name = 'james'
age = 18
address = '서울시 용산구 한남동'
scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}

with open('james.p', 'wb')as file: #james.p 파일을 바이너리쓰기모드(writebinary)로 열기
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

#unpickling하기
import pickle

with open('james.p', 'rb')as file:
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores  = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)


#파일에서 10자 이하인 단어 개수세기

#1.문자열파일만들기
words = ['anonymously\n',
        'compatibility\n',
        'dashboard\n',
        'experience\n',
        'photography\n',
        'spotlight\n',
        'warehouse\n']

with open('words.txt', 'w')as file:
    file.writelines(words)


#2 단어개수세기
with open('words.txt', 'r')as file:
    count = 0
    words = file.readlines()
    for word in words:
        if len(word.strip('\n')) <= 10:
            count += 1
    print(count)

#공백으로 문자열 분리 뒤 c가 존재하는 단어만 가져오기
with open('words.txt', 'r')as file:
    words = file.readlines()

    for word in words: #
        word2 = word.split() #
    
    for i in word2: 
        if 'c' in i: #
            print(i.strip(',.'))


#문자열을 응용하여 회문판별 및 N-gram만드는방법
#회문은 거꾸로 읽어도 제대로 읽은것과 같은문장임(level, SOS), 즉 가ㅏ운데 문자를 기준으로 왼쪽 오른쪽 문자가 같음.
#회문(palindrome)은 유전자 염기서열 분석, N-gram은 빅데이터 분석, 검색엔진에서 많이 쓰인다.

word = input('단어를 입력하세요')

is_palindrome = True #회문판별값을 저장할 변수, 초기값은 True
for i in range(len(word) // 2): #0부터 문자열 절반만큼 반복
    if word[i] != word[-1-i]: #왼쪽문자와 오른쪽 문자를 비교하여 문자가다르면 회문이 아님
        is_palindrome = False
        break
print(is_palindrome)
#판별시 문자열길이가 중요한데 홀수 길이면 가운데 글자 바로 앞까지만 검사하게됨.

#시퀀스 객체의 슬라이스를 활용하여 간단하게 판별하기
word = input('단어를입력하세요:')
print(word == word[::-1])#원래의 문자열과 반대로 뒤집은 문자열을 비교 # 전체에서 인덱스 1씩 감소시키면서 요소를 가져오므로 반대로 뒤집은것과 같음


#반복가능한 객체의 요소순서를 반대로 뒤집는 Reversed를 사용해도됨.
#list에 문자열을 넣으면 하나하나가 리스트의 요소로 들어가므로 비교 가능
word = 'level'
list(word) == list(reversed(word))

#join, reversed 메소드 사용하기
word = 'level'
word == ''.join(reversed(word))#join은 구분자 문자열과 문자열 리스트의 요소를 연결한다. 여기서 빈문자열''에 reversedword의 요소를 연결했으므로 문자순서가 반대로된 문자열을 얻을 수 있다


#N-gram은 문자열에서 N개의 연속된 요소를 추출하는 방법이다. 
#2-grma씩 출력하기
text = 'Hello'

for i in range(len(text)-1): #2gram이므로 홀수이니까 문자열 끝에서 한글자 앞까지만 반복
    print(text[i], text[i+1], sep = '') #현재문자와그다음문자 출력
for i in range(len(text)-2): #3gram
    print(text[i], text[i+1],text[i+2], sep='')

#단어단위 n-gram
text = 'this is python script'
words = text.split() #공백을 기준으로 문자열을 분리하여 리스트로 만듦

for i in range(len(words)-1):
    print(words[i], words[i+1])

#zip을 이용한 ngram
text = 'hello'

two_gram = zip(text, text[1:])
for i in two_gram:
    print(i[0], i[1], sep='')
#zip은 보통 리스트 두개를 딕셔너리로 만들때 사용했는데 위와 같이 사용하면 한개씩 밀린상태에서 각 문자를 묶은 튜플이 생성됨.

text = "this is python script"
words = text.split()
print(list(zip(words,words[1:])))

#zip에 일일히 text[0:], text[1:]등을 넣었던것을 반복문으로 바꿔서 처리해줌.
text = 'hello'
print([text[i:] for i in range(3)])

#zip은 반복가능한 객체 여러개를 콤마로 구분해서 넣어줘야 한다.
a= list(zip(['hello', 'ello', 'llo']))
print(a)
#이렇게하면  요소가 3개들어있는 list1개를 넣어준것이기 때문에  3gram으로 출력되는 것이안됨.
b=list(zip(*['hello','ello', 'llo']))
print(b) 
#zip에 각 요소를 콤마로 구분해서 넣어주려면 리스트앞에 *을 붙여야한다.
text = "hello"
c= list(zip(*[text[i:]for i in range(3)]))
print(c)
#이렇게 list 에 *을 붙이는 방법을 리스트언패킹이라고 한다.

#입력된 숫자에 해당하는 단어단위 N-gram을 튜플로 출력해보자.[만약 입력된 문자열의 단어개수가 입력된 정수 미만이라면 worng을 출력]
n = int(input())
text = input()
words = text.split() #입력된 한줄로 된 문자열 값은 split을 사용하여 분할한 뒤 words 변수에 저장

if (len(words) < n): #입력된 숫자n 보다 단어갯수가 적으면 wrong 출력
    print('wrong')
else: #문자열 리스트는*[words[i:]for i in range(n)]을 통해 n 만큼 반복하여 리스트로 만들어준
    n_gram = zip(*[words[i:]for i in range(n)])
    for i in n_gram:
        print(i)

#words.txt 파일에서 회문인 단어만 다시 가지고 나오는 코드
with open('words.txt','r')as file:
    words = file.readlines()
    for word in words:
        word = word.strip('\n')
        if word == word[::-1]:
            print(word)


def hello():
    print('Hello, world!')
hello()

#내용이 없는 빈함수를 만들기 위해서는 
def hello():
    pass

def add(a,b):
    print(a+b)
add(5, 7)
"""
"""
#함수에서 doc string 사용하기 doc string윗줄에 다른코드가 오면 안된다.
def add(a,b):
    """"""이 함수는 a,b를 더한 뒤 결과를 반환하는 함수 입니다 .""""""
    return a + b

x = add(10,20)
print(x)
print(add.__doc__) #함수의 독스트링을 출력하는 방법
help(add) #help 에 함수이름을 넣으면 이름,매개변수,독스트링을 도움말로 출력해준다.

def add(a,b):
    return a + b
#return을 사용하면 함수 바깥으로 반환 할 수 있다.

x = add(10,20)
print(x)
#이렇게 하면 반환값이 x 에 저장되는 것임
print(add(10,20))
#이리해도 무방

#매개변수가 없고 반환값만 있는 함수
def one():
    return 1
x = one()
print(x)


def not_ten(a):
    if a == 10:
        return # 이렇게 함수 중간에서 빠져나오게 사용한다 if 와 조합일 때 특정조건에서 함수중간에서 빠져나오기 위해 사용
    print(a, '입니다', sep = '')

print(not_ten(5))
print(not_ten(10))


def add_sub(a,b):
    return a+b, a-b

x,y = add_sub(10,20)
print(x)
print(y)

print(x,y) #이렇게 return으로 값을 여러개 반환하면 tuple이 반환된다.

def one_two():
    return (1,2) # return 1, 2  와 같다.

#함수 호출(스택다이어그램으로 알아보기)
#스택은 접시쌓기와 같이 접시를 차곡차곡쌓고 꺼낼때 위쪽부터 차례대로 꺼내는 방식이다.
#파이썬에서는 접시쌓기와 방향이 반대인데, 함수가 아래쪽 방향으로 추가되고 함수가 끝나면 위쪽방향으로 사라진다.

def mul(a, b):
    c = a * b
    return c

def add(a, b):
    c = a + b
    print(c)
    d = mul(a,b)
    print(d)

x = 10
y = 20
add(x,y)

#몫과 나머지를 출력하는 함수 만들기

x = 10
y = 3

def get_quotient_reaminder(a,b):
    return a//b , a%b

qoutient, reaminder = get_quotient_reaminder(x,y)
print('몫: {0}, 나머지:{1}'.format(qoutient, reaminder))


#사칙연산 반환 함수
x,y = map(int, input().split())
def calc(a,b):
    return a+b, a-b, a*b, float(a/b)

a,s,m,d = calc(x,y)
print('덧셈:{0}, 뺄셈:{1},곱셈:{2},나눗셈:{3}'.format(a,s,m,d))

#함수에 인수를 순서대로 넣는 방법을 인수(positional argument)라고 합니다. 인수의 위치가 정해져있는것.
print(10,20,30)
#위치 인수를 사용하는 함수를 만들고 호출하기
def print_numbers(a,b,c):
    print(a)
    print(b)
    print(c)
"""

