m = eval(input("Enter first integer: "))
n = eval(input("Enter second integer: "))

# gcd的初始值 
gcd = 1
# 可能的gcd值 
k = 2

# 朴素解法
while k <= m and k <= n:
    if m % k == 0 and n % k == 0:
        gcd = k 
    k += 1
    
print(m,"和", n, "的最大公约数是", gcd)
