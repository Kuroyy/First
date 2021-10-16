import turtle as t


def draw_square(side_lenght, x, y, line_color, fill_color):
    # настройка
    t.pencolor(line_color)
    t.fillcolor(fill_color)
    t.penup()
    t.goto(x, y)
    t.pendown()

    # рисование
    t.begin_fill()
    t.forward(side_lenght)
    t.left(90)
    t.forward(side_lenght)
    t.left(90)
    t.forward(side_lenght)
    t.left(90)
    t.forward(side_lenght)
    t.left(90)
    t.end_fill()

# Настройка черепахи
t.shape("turtle")
t.speed(1)


# рисование
draw_square(100, 0, 0, "#ff0000", "#0000ff")


t.done()