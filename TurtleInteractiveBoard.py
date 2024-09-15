import turtle


drawing_board2 =  turtle.Screen()
drawing_board2.bgcolor("light blue")
drawing_board2.title("Draw")

turtle_instance4 = turtle.Turtle()
def turtle_pen_up():
    turtle_instance4.penup()
def turtle_pen_down():
    turtle_instance4.pendown()
def turtle_forward():
    turtle_instance4.forward(100)
def rotate_angle_right():
    turtle_instance4.setheading(turtle_instance4.heading()-10)
def rotate_angle_left():
    turtle_instance4.setheading(turtle_instance4.heading()+10)
def screen_cleaner():
    turtle_instance4.clear()
def return_home():
    turtle_instance4.home()


drawing_board2.listen()
drawing_board2.onkey(fun = turtle_forward, key = 'space')
drawing_board2.onkey(fun = rotate_angle_right, key = 'Down')
drawing_board2.onkey(fun = rotate_angle_left, key = 'Up')
drawing_board2.onkey(fun = screen_cleaner,key = 'c')
drawing_board2.onkey(fun = return_home,key = 'x')
drawing_board2.onkey(fun = turtle_pen_up,key = 'q')
drawing_board2.onkey(fun = turtle_pen_down,key = 'e')

turtle.mainloop()