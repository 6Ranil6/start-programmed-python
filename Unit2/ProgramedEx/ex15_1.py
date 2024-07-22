# 15

# Подключаем черепаший модуль и настраиваем
import turtle
turtle.showturtle()
turtle.speed(3)
turtle.setup(1000, 600)

# Настроем фон и цвет заливки
turtle.fillcolor("red")
turtle.bgcolor("yellow")

# Выполняем пункт а)
# Рисуем стразу два ромба
turtle.begin_fill()
turtle.setheading(45)
turtle.forward(100)
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()

# Удаляем рисунок из пункта а)
turtle.reset()
turtle.fillcolor("green")
# Рисуем пункт б)

# Добавляем модуль  math для более точных подсчетов
import math

# Начинаем движение и ресуем внутренний треугольник
turtle.begin_fill()
turtle.left(45)
turtle.forward(100 * math.sqrt(2)) # один из катетов прямоугольного треугольника
turtle.right(90)
turtle.forward(100 * math.sqrt(2))
turtle.setheading(180)
turtle.forward(200)
turtle.end_fill()

# Рисуем внешний треугольник
turtle.goto(100, 200)
turtle.goto(200, 0)

# Удаляем рисунок пункта б)
turtle.reset()
turtle.pensize(3)
turtle.speed(3)

# Выполняем пункт в)
turtle.pencolor("red")

# вносим  координаты точек// учтем, что так надо было и в пукте а и в б
POINT_1_X = 0 
POINT_1_Y = 0

POINT_2_X = 0 
POINT_2_Y = 100

POINT_3_X = -100 
POINT_3_Y = 100

POINT_4_X = -100 
POINT_4_Y = 0

POINT_5_X = 0
POINT_5_Y = -100

POINT_6_X = 100 
POINT_6_Y = -100

POINT_7_X = 100 
POINT_7_Y = 0

# Рисуем каждое ребро по частям // находимся в точке (0, 0)

turtle.goto(POINT_2_X, POINT_2_Y)
turtle.goto(POINT_3_X, POINT_3_Y)
turtle.goto(POINT_4_X, POINT_4_Y)
turtle.goto(POINT_5_X, POINT_5_Y)
turtle.goto(POINT_6_X, POINT_6_Y)
turtle.goto(POINT_7_X, POINT_7_Y)
turtle.goto(POINT_1_X, POINT_1_Y)
turtle.goto(POINT_4_X, POINT_4_Y)
# не осталось свободных ребер... Перемещаемся не рисуя в точку 5 
turtle.penup()
turtle.goto(POINT_5_X, POINT_5_Y)
turtle.pendown()
# продолжаем рисовать ребра
turtle.goto(POINT_1_X, POINT_1_Y)
turtle.goto(POINT_2_X, POINT_2_Y)
turtle.goto(POINT_7_X, POINT_7_Y)
# не осталось свободных ребер... Перемещаемся не рисуя в точку 1 
turtle.penup()
turtle.goto(POINT_3_X, POINT_3_Y)
turtle.pendown()
# продолжаем рисовать ребра
turtle.goto(POINT_1_X, POINT_1_Y)
turtle.goto(POINT_6_X, POINT_6_Y)

# Конечные настройки
turtle.hideturtle()
turtle.done()
