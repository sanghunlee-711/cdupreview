"""
#81, 1082
a = input()
b = int(a,16)

for i in range(1,16,1):
    #print("%s*%X=%X" %(a,i,b*i))
    print("{}*{:X}={:X}".format(a,i,b*i))
    #2진수 :#b, 16진수: #x, 8진수: #o
    # 해당자료형 변환에 # 삽입시 앞에 ox가 뜬다 (제거하면 안뜸)

#82, 1083
a = int(input())
for i in range(1, a+1, 1):
    if i % 3 == 0:
        print('X')
    else:
        print(i)

#83, 1084
r, g, b = map(int,input().split())

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k)



list = [(x,y,z) for x in range(r) for y in range(g) for z in range(b)]
for i in list:
   print (i) # 이렇게하면 값이 tuple로 나온다.


#84,1085
h,b,c,s = map(int ,input().split())
multiple = (h*b*c*s/(8*1024*1024)) 
print("{0:.1f} MB".format(multiple))
# 포맷팅에서의 소수법 표기는 0:.1f면 소수점 한자리까지 .2면 두자리겠지 

#85, 1086
w,h,b = map(int ,input().split())
storage = (w*h*b/(8*1024**2))
print("{:.2f} MB".format(storage))

#86, 1087
a = int(input())
sum = 0
for i in range(1, a+1, 1):
    sum += i
    if sum >= a:
     break
print(sum)

#87, 1088
a = int(input())
for i in range(1,a+1,1):
    if i%3 != 0:
        print(i, end=" ")


b = []
for i in range(1,a+1,1):
    if i % 3 != 0:
        b.append(i)
print(b)
# 이렇게하면 출력값이 list이니까 안될테고 ..
end = "" 를 쓰면될듯

#88, 1089
a,d,n= map(int, input().split())
e=a+(n-1)*d
print(e)

#89,1090
a,r,n = map(int,input().split())
what = a*r**(n-1)
print(what)
"""
#90, 1091
a, m ,d ,n =map(int, input().split())
#what = a*(n-1)*(m*(n-1)+d)
for i in range(0,n-1,1):
    a = a*m+d

print(a)
