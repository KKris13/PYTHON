import random
import turtle

turtle.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]
for n in range(50):
    # Generate spirals of random sizes/colors at random locations
    turtle.pencolor(random.choice(colors))   # Pick a random color 
    size = random.randint(10,40)        # Pick a random spiral size
    # Generate a random (x,y) location on the screen
    x = random.randrange(-turtle.window_width()//2, turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2, turtle.window_height()//2)
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()
    for m in range(size):
        turtle.circle(m*2)
        turtle.left(91)

