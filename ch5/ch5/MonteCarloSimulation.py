import random

# 总点数，常量
N = 1000

#落在圆内的点数
m = 0

for i in range(N):
    x = random.uniform(-1,1) 
    y = random.uniform(-1,1) 

    if x * x + y * y <= 1:
        m += 1

pi = 4 * m / N

print("PI is", pi)
