from random import*
from time import clock
N=2**30
m=0
clock()
for i in range(N):
    X=uniform(-1,1)
    Y=uniform(-1,1)
    if X*X+Y*Y<=1:
        m+=1
pi=4*(m/N)
print("pi=:",pi)
print("运行时间是：{:.9f}s".format(clock()))
