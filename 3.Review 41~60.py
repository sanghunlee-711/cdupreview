#41, 1044
a = int(input())
print(a+1)

#42, 1045
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a/b)

#43, 1046
a = int(input())
print(a%b)

#44, 1047
a = int(input())
print(a*2)

#45, 1048
a, b = map(int,input().split())
print(a*(2**b))

#46, 1049
a, b = map(int, input().split())
if a > b:
    print(1)
else:
    print(0)

#47, 1050
a, b = map(int, input().split())
if a == b:
    print(1)
else:
    print(0)

#48,1051
a, b = map(int, input().split())
if b >= a:
    print(1)
else:
    print(0)

#49, 1052
a, b = map(int, input().split())
if a != b:
    print(1)
else:
    print(0)

#50, 1053
a = map(int, input()) # Input only 1 or 0
if a == 1:
    print(0)
elif a == 0:
    print(1)

#51, 1054
a, b = map(int,input().split()) # Input only 1 or 0
if a == 1 and b == 1:
    print(1)
else:
    print(0)

#52, 1055
a, b = map(int, input().split()) # Input only 1 or 0
if a == 1 or b == 1:
    print(1)
else:
    print(0)

#53, 1056
a, b = map(int, input().split()) # Input only 1 or 0
if a != b:
    print(1)
else:
    print(0)

#54, 1057
a, b = map(int, input().split()) # Input only 1 or 0
if a == b:
    print(1)
else:
    print(0)

#55, 1058
a, b = map(int, input().split()) # Input only 1 or 0
if a == 0 and b == 0:
    print(1)
else:
    print(0)

#56, 1059
a = int(input())
print(~a)

#57, 1060

a, b = map(int, input().split())
print(a&b)

#58, 1061
a, b = map(int, input().split())
print(a|b)

#59, 1062
a, b = map(int, input().split())
print(a^b)

#60, 1063
a, b = map(int, input().split())
if a > b:
    print(a)
elif a < b:
    print(b)
