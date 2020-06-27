num = int(input('enter the five  digits'))
x = num // 10000
x1 = (num - x * 10000)//1000
x2 = (num - x* 10000 - x1*1000)//100
x3 = (num - x * 10000 - x1* 1000 - x2*100)//10
x4 = num - x * 10000 - x1* 1000 - x2*100 - x3*10
sums = x+x1+x2+x3+x4
print(sums)