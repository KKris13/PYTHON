m = eval(input("Enter first integer: "))
n = eval(input("Enter second integer: "))

while n % m !=0:
    m, n = n % m, m
    
print("最大公约数是", m)
