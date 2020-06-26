import turtle

t = turtle.Turtle()

def drawDiag(t, a):
    t.right(45)
    t.forward(a)
    t.right(180)
    t.forward(a)
    t.right(135)


def drawThreeD(t, a, b, c):
    t.forward(b)
    drawDiag(t, a)
    t.right(90)
    t.forward(c)
    t.left(90)
    drawDiag(t, a)
    t.left(180)
    t.forward(b)
    t.right(180)
    drawDiag(t, a)
    t.left(90)
    t.forward(c)
    t.right(90)
    drawDiag(t, a)
    t.right(45)
    t.forward(a)
    t.left(45)
    t.forward(b)
    t.right(90)
    t.forward(c)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.forward(c)
    t.right(90)

# a is the length of the diagonal
# b is the length of the horizontal sides
# c is the length of the vertical sides
