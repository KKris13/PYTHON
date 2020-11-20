import random
import time

# 生成1到100间的随机数
number = random.randint(1, 100)
guess = -1
count = 0
start  = time.time()
while guess != number:
    guess = eval(input("Enter your guess between 1 and 100: "))
    if guess == number:
        print("猜对了！")
        count += 1
    elif guess > number:
        print("高了！")
        count += 1
    else:
        print("低了！")
        count += 1
end  = time.time()
print('你共猜了', count,'次，', '用时', int(end-start), '秒。')



