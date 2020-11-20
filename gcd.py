p,q = map(int, input("enter p & q:").split())#输入两个数p和q
gcd=1
while 1:
    if q==0:
        gcd= p
        break
    else:
        p,q=q,p%q
    

print(gcd)#输出公约数gcd
