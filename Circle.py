import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("white")
turtle_screen.title("Turtle Python")

turtle_instance4 = turtle.Turtle()
turtle_instance4.color("black")
turtle_colors = ["red", "purple", "blue", "green", "orange"]
turtle.speed(1)

for i, color in enumerate(turtle_colors): #enumerate ile hem indekslere hem de elemanlara erişmiş olduk
    turtle_instance4.circle(10*(i+1))
    turtle_instance4.circle(-10*(i+1))
    turtle_instance4.left(45)  # 45 derece dönmesini sağlıyoruz
    turtle_instance4.color(color)  # Rengi değiştiriyoruz

turtle.mainloop()
