"""
# 61, 1064
a, b, c = map(int, input().split())
print(min(a,b,c))
#62, 1065
a, b, c = map(int, input().split())
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)
"""
"""
#63, 1066
a, b, c = map(int, input().split())
if a%2 == 0:
    print('even')
else:
    print('odd')
if b%2 == 0:
    print('even')
else:
    print('odd')
if c%2 == 0:
    print('even')
else:
    print('odd')
"""
#65, 1067
a = int(input())

if a  > 0:
    print('plus')
elif a < 0:
    print('minus')

if a %2  == 0:
    print('even')
else:
    print('odd')