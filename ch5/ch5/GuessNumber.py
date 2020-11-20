import random

# 生成1到100间的随机数
number = random.randint(1, 100)

guess = -1

while guess != number:
    guess = eval(input("Enter your guess between 1 and 100: "))
    if guess == number:
        print("猜对了！")
    elif guess > number:
        print("高了！")
    else:
        print("低了！")



