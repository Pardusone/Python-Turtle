import turtle

drawing_board = turtle.Screen() #ekranı oluşturduk
drawing_board.bgcolor("light blue") #ekranın rengini ayarladık (renk kodunu başına # koyarak da ayarlayabiliriz)
drawing_board.title("Python Turtle") #başlık koyduk

turtle_instance = turtle.Turtle()
side_number = int(input("Kac kenarli oldugunu giriniz"))

aci = 360.0/side_number
for i in range(side_number):
    turtle_instance.right(aci)
    turtle_instance.forward(30)

turtle.done()

