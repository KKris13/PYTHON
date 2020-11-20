# Prompt the user to enter a radius
radius = int(input("Enter a number for radius: "))

#Check the input
if radius < 0:
    print("Incorrect input")
else:
    area = radius * radius * 3.14159
    print("The area for the circle of radius", radius, "is", area)
    
