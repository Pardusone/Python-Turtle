import turtle
# from polygon import turtle_instance2  # Comment this out if not needed

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("white")
turtle_screen.title("Turtle Python")

turtle_instance2 = turtle.Turtle()  # Create a new instance
turtle_instance2.color("black")

def shrinkingSquare(size):
    for i in range(4):
        turtle_instance2.forward(size)
        turtle_instance2.left(90)
        size = size - 5
shrinkingSquare(150)
shrinkingSquare(130)
shrinkingSquare(120)
shrinkingSquare(110)
shrinkingSquare(100)
shrinkingSquare(90)
shrinkingSquare(80)
shrinkingSquare(70)
shrinkingSquare(150)
shrinkingSquare(130)
shrinkingSquare(120)
shrinkingSquare(110)
shrinkingSquare(100)
shrinkingSquare(90)
shrinkingSquare(80)
shrinkingSquare(70)


turtle.done()
