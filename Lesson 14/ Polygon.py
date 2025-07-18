import turtle 
turtle.Screen().bgcolor("white")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
numsides = 6
sidelen = 95
angle = 360/numsides
for i in range(numsides):
    polygon.forward(sidelen)
    polygon.right(angle)
turtle.done()


