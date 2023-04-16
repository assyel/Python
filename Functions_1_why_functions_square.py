import turtle
# 4 давайте избавимся от повторения 2 интструкции 4 раза. для этого создадим еще одну функцию
def move(a):
    turtle.forward(a)
    turtle.left(90)
# 3 чтобы избавиться от избыточности кода, создаем функцию под import turtle
def drawSquare(a):
    # 1 и внутри нее размещаем наши 8 инструкции
#turtle.speed(1)
# 5 удаляем эти 8 инструкции, вместо них напишем цикл loop 
# и должны вызывать те 2 инструкции 4 раза
    for i in range(4):
        # и вызываем цикл 
        move(a)
# 7 расскрасим
def drawSquareColor(a, color):
    # 9 чтобы цвет залить, 
    # надо написать следующий код turtle.color(color)
    turtle.color(color)
    turtle.begin_fill()
    # 10 чтоб не было повторения этих кодов for i in range(4):    move(a)
    # мы просто можем вызвать drawSquare(a) 
    # и получим аналогичный результат
    # for i in range(4):
    #     move(a)
    drawSquare(a)
    turtle.end_fill()
    # turtle.forward(100)
    # turtle.left(90)
    # turtle.forward(100)
    # turtle.left(90)
    # turtle.forward(100)
    # turtle.left(90)
    # turtle.forward(100)
    # turtle.left(90)
# 6 чтоб получить квадраты разной длины, нам 
# надо drawSquare() передавать длину квадрата 60 и 120.
# Из за того что передали длину квадрата теперь наша 
# функция должна принимать какой то аргумент. давайте 
# дадим имя a drawSquare()
# 8 через запятую передадим цвет
drawSquareColor(60, 'red')
turtle.goto(150, 150)
drawSquareColor(120, 'blue')
# 2 а этот блок удаляем, я закомментирую
    # turtle.forward(100)
    # turtle.left(90)
    # turtle.forward(100)
    # turtle.left(90)
    # turtle.forward(100)
    # turtle.left(90)
    # turtle.forward(100)
    # turtle.left(90)

