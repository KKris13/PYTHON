data = eval(input("输入一个正整数（输入0表示结束）："))

sum = 0
while data != 0:
    sum += data
    data = eval(input("输入一个正整数（输入0表示结束）："))

print("和为：", sum)
