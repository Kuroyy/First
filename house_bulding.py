import turtle as t


def build_house(base_x = -500, base_y = -500, base_width = 100, base_height = 10, base_fill = "#000000", walls_width = 20, walls_height = 20, walls_fill = "#000000", roof_width = 0, roof_height = 0, roof_fill = "#000000"):
    """
        base_x — X левого нижнего угла фундамента
        base_y — Y левого нижнего угла фундамента
        base_width — ширина фундамента
        base_height — высота фундамента
        base_fill — цвет заливки фундамента

        walls_x - считаем автоматически
        walls_y - считаем автоматически
        walls_width - считаем автоматически
        walls_height - спрашиваем у заказчика
        walls_fill - спрашиваем у заказчика

        roof_x - считаем автоматически
        roof_y - считаем автоматически
        roof_width - спрашиваем у заказчика
        roof_height - спрашиваем у заказчика
        roof_fill - спрашиваем у заказчика
    """
    t.speed(0)

    # считаем автоматические величины
    walls_x = base_x
    walls_y = base_y + base_height
    walls_width = base_width
    roof_x = walls_x - (walls_width * 0.1)
    roof_y = base_height + walls_height
    roof_width = walls_width * 1.2
    roof_angle = 35
    

    def build_base(base_x, base_y, base_width, base_height, base_fill):
        t.penup()
        t.goto(base_x, base_y)
        t.setheading(0)
        t.fillcolor(base_fill)
        t.pendown()
        t.begin_fill()
        t.forward(base_width)
        t.left(90)
        t.forward(base_height)
        t.left(90)
        t.forward(base_width)
        t.left(90)
        t.forward(base_height)
        t.end_fill()


    def build_walls(walls_x, walls_y, walls_width, walls_height, walls_fill):
        t.penup()
        t.goto(walls_x, walls_y)
        t.setheading(0)
        t.fillcolor(walls_fill)
        t.pendown()
        t.begin_fill()
        t.forward(walls_width)
        t.left(90)
        t.forward(walls_height)
        t.left(90)
        t.forward(walls_width)
        t.left(90)
        t.forward(walls_height)
        t.end_fill()


    def build_roof(roof_x, roof_y, roof_height, roof_width, roof_angle):
        t.penup()
        t.goto(roof_x, roof_y)
        t.setheading(0)
        t.fillcolor(roof_fill)
        t.pendown()
        t.begin_fill()
        t.forward(roof_width)
        t.left(roof_angle)
        t.forward(145)
        t.left(-70)
        t.forward(145)
        t.left(-145)
        t.forward(238)
        t.end_fill()
        t.penup()
        t.goto(10, 10)

    build_base(base_x, base_y, base_width, base_height, base_fill)
    build_walls(walls_x, walls_y, walls_width, walls_height, walls_fill)
    build_roof(roof_x, roof_y, roof_width, roof_height, roof_angle)


build_house(base_x = 0, base_y = 0, base_width = 200, base_height = 10, base_fill = "#660000", walls_height = 150, walls_fill = "orange", roof_fill = "red", roof_width = 100)
t.done()
