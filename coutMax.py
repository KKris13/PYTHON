#找出最大数及计数
import math
Max=-math.inf
count=0
x=1
while x!=0:
    x=int(input("emter a number(0,for end of input):"))
    if x!=0 and x>Max:#如果x被替换了就重新计数
        Max=x
        count=1
    elif x!=0 and x==Max:#最大值max重复出现
        count+=1
print("the largest number is:",Max)
print("The occurrence count of the largest number is:",count)
        
