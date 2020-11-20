import random
import turtle

turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]

size = random.randint(10,100)

turtle.pencolor(random.choice(colors))
turtle.circle(size)
turtle.done()
        

