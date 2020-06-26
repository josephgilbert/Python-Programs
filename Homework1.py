import turtle

t = turtle.Turtle()

def drawDiag(t):
    t.right(45)
    t.forward(40)
    t.right(180)
    t.forward(40)
    t.right(135)


def drawThreeD(t):
    t.forward(50)
    drawDiag(t)
    t.right(90)
    t.forward(50)
    t.left(90)
    drawDiag(t)
    t.left(180)
    t.forward(50)
    t.right(180)
    drawDiag(t)
    t.left(90)
    t.forward(50)
    t.right(90)
    drawDiag(t)
    t.right(45)
    t.forward(40)
    t.left(45)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
