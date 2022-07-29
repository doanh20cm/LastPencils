# put your python code here
a = int(input())
tong = 0
sum_sqr = 0
tong += a
sum_sqr += a ** 2
while tong != 0:
    a = int(input())
    tong += a
    sum_sqr += a ** 2
    if tong == 0:
        print(sum_sqr)
        break
else:
    print(0)