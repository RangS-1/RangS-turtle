import turtle

t = turtle.Turtle()
t.penup()
t.goto(-250, -250)
t.pendown()

for i in range(3):
    t.forward(500)
    t.left(120)

turtle.done()
