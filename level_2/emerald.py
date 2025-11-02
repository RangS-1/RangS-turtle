import turtle

t = turtle.Turtle()

t.penup()
t.goto(-200, -250)
t.pendown()

for i in range(4):
    t.color("green")
    t.forward(400)
    t.left(45)
    t.forward(50)
    t.left(45)

turtle.done()
#can anyone help me how to fill the shape?
