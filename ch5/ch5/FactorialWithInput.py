n = int(input('Factorial for(enter -1 to stop)：'))
while n >= 0:
    prod = 1
    for i in range(2, n+1):
        prod = prod * i
    print('The factorial of', n, 'is', prod)
    n = int(input('Factorial for(enter -1 to stop)：'))
