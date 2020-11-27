import turtle as t

def Drawbianxing():
    j=int(input("number:"))
    i=360.0/j
    p=i
    for x in range(j):
        t.fd(50)
        t.seth(p)
        p=p+i

def DrawFiveStar():
    q=36
    for x in range(5):
        t.seth(q)
        t.fd(200)
        q=q+144

t.setup(2000,2000,200,200)
t.penup()
t.fd(-200)

t.pendown()
t.pensize(25)
t.color("blue")


DrawFiveStar()
    
t.done()
