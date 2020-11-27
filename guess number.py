#彩票小游戏
import random
#产生随机两位数数字
x=random.randint(10,99)
x1=x%10
x2=x//10
#用户输入数字
guess=int(input("Enter your lottery pick（two digits）："))
g1=guess%10
g2=guess//10
print("the lottery number is :",x)
#判断中多少钱
if guess== x:
    print("match two digits in order ,win ¥10000")
elif x1==g2 and x2==g1:
    print("match two digits  in disorder,win ¥3000")
elif x1==g1 and x2 !=g2 or x1!=g1 and x2==g2:
     print("match one digit,win ¥1000")
else:
    print("you lose")
