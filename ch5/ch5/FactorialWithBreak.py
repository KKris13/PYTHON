while True:
    n = int(input('Factorial for(enter -1 to stop)：'))
    
    if n < 0:
        break
    
    prod = 1
    for i in range(2, n+1):
        prod = prod * i
    print('The factorial of', n, 'is', prod)
print('Bye!')
