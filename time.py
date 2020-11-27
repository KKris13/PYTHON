import time
currentTime=time.time()
'''for i in range(1,1000):
    print(i)
    i=i+1
s2=time.time()
print(s2-s1)

totalSeconds=int(currentTime)
totalMinute=totalSeconds//60
currentSeconds=totalSeconds%60
totalHours=totalMinute//60
currentMinute=totalMinute%60
print(totalHours," ",currentMinute," ",currentSeconds)'''
print(time.asctime())
print(time.localtime())
print(time.strftime("%Y-%m"))
