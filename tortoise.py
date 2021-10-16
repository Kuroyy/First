import turtle as t


def draw_rectangle(width, height, line_color, fill_color):
    t.goto(0, 0)
    t.pencolor(line_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    
draw_rectangle(400, 200, "orange", "green")
draw_rectangle(200, 100, "red", "blue")



t.done()