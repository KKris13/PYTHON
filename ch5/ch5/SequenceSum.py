a = int(input('首项：'))
b = int(input('末项：'))
c = int(input('公差：'))

s = 0
for i in range(a, b+1, c):
    s = s + i

print('等差序列的和为：',  s)
