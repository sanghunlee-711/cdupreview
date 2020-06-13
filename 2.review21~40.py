
#21,1023
a, b = input().split('.')
print(a)
print(b)
#22,1024
a = input()
for i in range(len(a)):
    print('%s' %a[i])
#23,1025
a = input()
for i in range(len(a)):
    print("[%d]" %(int(a[i]) * 10**(len(a)-(i+1))))
#24, 1026
a, b, c = map(int,input().split(":"))
print(b)
#25, 1027
a, b, c = map(int,input().split("."))
print("{}-{}-{}".format(c,b,a)) # 포맷팅 출력 갯수 지정 알아보기
#26, 1028 #27, 1029 # 28, 1030
a = input()
a = int(a)
print(a)
#29, 1031
a = input()
a = int(a)
print("%o" %a)
#print(int(a, 8)) # int 에서의 사용은 문자열 - > 정수형이지 정수형끼리는 안됨.
#30, 1032
a = input()
a = int(a)
#print("{:#x}".format(a))
print("%0x" %a)

#31, 1033
a = input()
print("%d" %int(a,16))

#32, 1034