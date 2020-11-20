import turtle

turtle.speed(0)

# 输入边数
sides = int(input("How many sides in your spiral?"))

colors=['red', 'yellow', 'blue', 'green', 'purple', 'orange']

# 外循环，共画70个多边形和玫瑰花瓣
for m in range(5,75):   
    turtle.left(91)
    turtle.penup()        
    turtle.forward(m*4)   # 移动到下一个角
    turtle.pendown()      
    # 在偶数角画小玫瑰花瓣
    if (m % 2 == 0):
        for n in range(sides):
            turtle.pencolor(colors[n%sides])
            turtle.circle(m/3)
            turtle.right(360/sides)
    # 在奇数角画小多边形
    else:
        for n in range(sides):
            turtle.pencolor(colors[n%sides])
            turtle.forward(m)
            turtle.right(360/sides)
