
#1,1001
print("Hello")
#2,1002
print("Hello World")
#3,1003
print("Hello\n" "World")
#4,1004
print("'Hello'")
#5,1005
print('"Hello World"')
#6,1006
print('!@#$%^&*()"')
#7,1007
print('"C:\\Download\\hello.cpp"')
#8,1008
print("\u250c\u252c\u2510")
print("\u251c\u253c\u2524")
print("\u2514\u2500\u2508")
#9,1010
a = int(input())
print(a)
#10,1011
a = input()
print(a)
#11,1012
a = input()
print("%f" %a)
#12,1013

a, b = input().split()
print(a, b)
#13,1014
a, b = input().split()
print(b, a)
#14,1015
a = input()
print("%.3f" %a)
#15,1017
a = input()
print(a, a, a)
#16,1018
a, b = input().split(':')
print(a, b, end = ":" )

#17,1019---------------------!
y, m, d = input().split(".")
y = int(y)
m = int(m)
d = int(d)
#print("{}.{2}.{2}".format(y,m,d))
print("%4d.%2d.%2d" %(y, m,d)) #-> formating으로 하는 방법 찾아보기

#18,1020
a, b = input().split("-")
print(a+b) #  문자열 같이 나오게 하는건 + 이다!
#19,1021
a = input()
print(a)
#20,1022
a = input()
print(a)
