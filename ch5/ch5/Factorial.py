n = int(input('Factorial for：'))

prod = 1
for i in range(2, n+1):
    prod = prod * i

print('The factorial of', n, 'is', prod)
