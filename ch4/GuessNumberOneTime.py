import random

# 生成1到100间的随机数
number = random.randint(1, 100)

# 提示用户输入所猜的数字
guess = eval(input("Enter your guess between 1 and 100: "))

if guess == number:
    print("猜对了！")
elif guess > number:
    print("高了！")
else:
    print("低了！")
