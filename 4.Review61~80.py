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

#66, 1068

a = int(input())

if 100 >= a >= 90:
    print("A")
elif 89>= a >=70:
    print("B")
elif 69>= a >=40:
    print("C")
elif 39>= a >=0:
    print("D")

#67, 1069

a = input()

if(a == "A"):
    print("best!!!")
elif(a == "B"):
    print("good!!")
elif(a == "C"):
    print("run!")
elif(a == "D"):
    print("slowly~")
else:
    print("what?")
    
#68, 1070
a = int(input())

if (a == 12 or a == 1 or a == 2):
    print("winter")
elif(a == 3 or a ==4 or a == 5):
    print("spring")
elif(a == 6 or a == 7 or a == 8):
    print("summer")
elif(a == 9 or a == 10 or a ==11):
    print("fall")

#69, 1071
a = list(map(int, input().split()))
i = 0

for i in range(0, len(a)-1):
    if a[i] == 0:
        break
    else:
        print(a[i]) # 안되는 이유 알아봐야할듯.
#70, 1072


n = int(input())
a = list(map(int, input().split()))

for i in range(0, n):
    print(a[i])


#71, 1073

a = list(map(int, input().split()))

if (a[i] != 0):
    print(a)[i]
else:
    break;

#72, 1074

a = int(input())

while (a != 0):
    print(a)
    a -= 1

#73, 1075

a = int(input())

while (a != 0):
    print(a-1)∫
    a -= 1
#74, 1076
"""
a = input()
b = ord(a)
i = ord('a') # a의 아스키 코드값이 필요하니
while ( i <=  b):
    print(chr(i), end=" ")
    i = i+1

#75
