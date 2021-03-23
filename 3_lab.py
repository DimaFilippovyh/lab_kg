import math
from turtle import *
import os 





def draw_coord():
    cor = Turtle()
    cor.hideturtle()
    cor.speed(0)
    cor.pensize(3)
    cor.up()
    cor.goto(0, -600)
    cor.down()
    cor.goto(0, 600)

    cor.up()
    cor.goto(-600, 0)
    cor.down()
    cor.goto(600, 0)


def draw_section():
    cor = Turtle()
    cor.hideturtle()
    cor.speed(0)
    tmp_point = -600
    i = 0
    while tmp_point != 600:
        cor.up()
        cor.goto(tmp_point, -600*pow(-1, i))
        cor.down()
        cor.goto(tmp_point, 600*pow(-1, i))
        tmp_point += 50

    i = 0
    tmp_point = -600
    while tmp_point != 600:
        cor.up()
        cor.goto(-600*pow(-1, i), tmp_point)
        cor.down()
        cor.goto(600*pow(-1, i), tmp_point)
        tmp_point += 50


point = Turtle()
point.speed(3)
point.hideturtle()
def draw_dot(x, y):
    point.up()
    point.goto(x, y)
    point.down()
    point.dot(9, "red")


def line(A, B, turt):
    x1, y1 = A
    x2, y2 = B

    x1, y1, x2, y2 = x1*50, y1*50, x2*50, y2*50

    cor = turt
    cor.hideturtle()
    cor.speed(0)
    cor.pensize(2)
    cor.up()
    cor.goto(x1, y1)
    cor.down()
    cor.goto(x2, y2)

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 50 if x1 < x2 else -50
    sy = 50 if y1 < y2 else -50
    err = dx - dy

    while True:
        draw_dot(x1, y1)

        if (x1 == x2) and (y1 == y2):
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
    
        if e2 < dx:
            err += dx
            y1 += sy



def circle(A, R, turt):
    x1, y1 = A
    x1, y1, R = x1*50, y1*50, R*50

    cor = turt
    cor.hideturtle()
    cor.speed(0)
    cor.pensize(2)
    cor.up()
    cor.goto(x1, y1-R)
    cor.down()
    cor.circle(R)

    x = R
    y = 0
    error = 50 - x
    while x >= y:
        draw_dot(x1 + x, y1 + y)
        draw_dot(x1 + y, y1 + x)
        draw_dot(x1 - x, y1 + y)
        draw_dot(x1 - y, y1 + x)
        draw_dot(x1 - x, y1 - y)
        draw_dot(x1 - y, y1 - x)
        draw_dot(x1 + x, y1 - y)
        draw_dot(x1 + y, y1 - x)
        y += 50
        if error < 0:
            error += 2 * y + 50
        else:
            x -= 50
            error += 2 * (y - x + 50)




def main():
    t = Turtle()
    t.screen.setup(1200, 1000)
    t.screen.title("Welcome to the lab 3!")
    t.speed(0)
    t.hideturtle()

    draw_coord()
    draw_section()

    cor = Turtle()

    while True:
        os.system("clear")

        print("""
            1 - Отрезок,
            2 - Окружность,
            3 - Очистить

            """)
        n = int(input("Что хотите увидеть? \n"))

        if n == 1:
            print('Введите координаты концов отрезка.')
            a = int(input('Первая точка x = ')), int(input('y = '))
            b = int(input('Вторая точка x = ')), int(input('y = '))
            line(a, b, cor)

        elif n == 2:
            print('Введите координаты центра и радиус.')
            a = int(input('Точка x = ')), int(input('y = '))
            r = int(input('Радиус = '))
            circle(a, r, cor)

        elif n == 3:
            cor.clear()
            point.clear()

        else:
            print("bye-bye")
            break


    t.screen.exitonclick()
    t.screen.mainloop()





if __name__ == "__main__":
    main()












