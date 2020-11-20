import sys
import time
m = eval(input("输入一个大于1的正整数: "))

i = 2
start = time.time()
while i < m:
    if m % i == 0:
        print(m,'不是素数。')
        sys.exit()
    i += 1
end = time.time()
print(m,"是素数，用时",int(end-start),"秒。")
