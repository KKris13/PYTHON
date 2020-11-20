import time
start = time.time()
for i in range(10):
    for j in range(10):
        for k in range(10):
            print(i , j, k)
end = time.time()
print("用时", int(end - start), "秒。")

