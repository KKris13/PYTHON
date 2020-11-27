#计算个人所得税收
wages=int(input("please enter you wages:"))

Wset=[3000,12000,25000,35000,55000,80000]#每级最高应纳税收所得额
rate=[0.03,0.10,0.20,0.25,0.30,0.35,0.45]#对应不同区间的税率
kouchushu=[0]
kouchushu*=7

#计算扣除数,本级速算扣除额=上一级最高应纳税所得额×(本级税率-上一级税率)+上一级速算扣除数
for i in range(0,6):
    a= rate[i+1]
    b= rate[i]
    kouchushu[i+1]=round(kouchushu[i]+Wset[i]*(a-b),3)#计算的浮点数有误差，去掉误差位

#print(kouchushu)
#计算超出5000的部分
restW=wages-5000

#计算所得税
if restW<=0:
    tax=0
elif restW<=3000:
    tax=restW*rate[0]-kouchushu[0]
elif restW<=12000 :
    tax=restW*rate[1]-kouchushu[1]
elif restW<=25000:
    tax=restW*rate[2]-kouchushu[2]
elif restW<=35000:
    tax=restW*rate[3]-kouchushu[3]
elif restW<=55000:
    tax=restW*rate[4]-kouchushu[4]
elif restW<=80000:
    tax=restW*rate[5]-kouchushu[5]
else:
    tax=restW*rate[6]-kouchushu[6]
    
print("tax=",tax)

