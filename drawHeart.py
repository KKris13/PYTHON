import turtle as t


t.speed(0)

def curvemove():
    for i in range(200):
        t.right(1)
        t.forward(1)

t.color('purple')
t.begin_fill()
t.left(140)
t.forward(111.65)

curvemove()
t.left(120)


curvemove()
t.color('red')
t.forward(111.65)
t.end_fill()

t.penup()
t.goto(-40,-50)
t.pendown()
t.write('',font=('SimHei',15,'bold'))
t.hideturtle()
t.end()
