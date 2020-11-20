import random
import turtle

turtle.speed(0)

colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]
for n in range(50):
    # Generate spirals of random sizes/colors at random locations
    turtle.pencolor(random.choice(colors))   # Pick a random color 
    size = random.randint(10,100)        # Pick a random spiral size
    # Generate a random (x,y) location on the screen
    x = random.randrange(-turtle.window_width()//2, turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2, turtle.window_height()//2)
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()
    turtle.circle(size)
        

