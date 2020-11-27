#求完全数
from time import*
start=time()
for i in range(2,10001):#循环2——10000的数
    sum=0
    for j in range(1,i):#寻找因子
        if i%j==0:
            sum+=j
    if sum==i:#如果因子之和等于本身则是完全数
        print(i,"是完全数")
end=time()
print("所用时间是",end-start)
 
