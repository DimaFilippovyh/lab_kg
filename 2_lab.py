from turtle import *
import numpy as np
from icecream import ic
from math import radians, cos, sin


t = Turtle()


lst_point = [(300.00, 350.00), (358.78, 330.90), (395.11, 280.90), (395.11, 219.10), (358.78, 169.10), \
             (300.00, 150.00), (241.22, 169.10), (204.89, 219.10), (204.89, 280.90), (241.22, 330.90)]

lst_point = [(300.00, 350.00, 1), (358.78, 330.90, 1), (395.11, 280.90, 1), (395.11, 219.10, 1), (358.78, 169.10, 1), \
             (300.00, 150.00, 1), (241.22, 169.10, 1), (204.89, 219.10, 1), (204.89, 280.90, 1), (241.22, 330.90, 1)]

def draw_coord():
    cor = Turtle()
    cor.speed(0)
    cor.up()
    cor.goto(0, -600)
    cor.down()
    cor.goto(0, 600)

    cor.up()
    cor.goto(-600, 0)
    cor.down()
    cor.goto(600, 0)


# def point_figure():
#     # centr 300 250
#     t.up()
#     t.goto(300, 250)
#     t.setheading(90)

#     t.speed(5)

#     #t.goto(300, 250)

#     for i in range(10):
#         t.down()
#         t.fd(100)
#         lst_point.append(t.pos())
#         t.goto(300, 250)
#         t.rt(36)

#     print(lst_point)


def draw_figure(lst):
    t.up()
    t.goto(lst[0][0], lst[0][1])
    t.down()
    i = 3
    while True:
        t.goto(lst[i][0], lst[i][1])
        if i == 0:
            break
        i += 3
        if i >= 10:
            i %= 10


def mul_martic(a_, b_):
    a = np.array(a_)
    b = np.array(b_)
    ic(a.dot(b))
    return a.dot(b)


def shift_figure(check, c):
    tmp_lst = []
    if check == 1:
        for i in lst_point:
            tmp_lst.append(mul_martic([[1, 0, c], [0, 1, 0], [0, 0, 1]], i))
    elif check == 2:
        for i in lst_point:
            tmp_lst.append(mul_martic([[1, 0, 0], [0, 1, c], [0, 0, 1]], i))
    else:
        print("Не то число")
        return lst_point

    ic(tmp_lst)
    return tmp_lst


def mirror_figure(check):
    if check == 1:
        tmp_lst = mul_martic(lst_point, [[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
    elif check == 2:
        tmp_lst = mul_martic(lst_point, [[1, 0, 0], [0, -1, 0], [0, 0, 1]])
    else:
        print("Не то число")
        return lst_point

    return tmp_lst


def mirror_line_figure():
    return mul_martic(lst_point, [[0, 1, 0], [1, 0, 0], [0, 0, 1]])


def scale_figure(check, ind):
    # return mul_martic(lst_point, [[ind, 0, 0], [0, ind, 0], [0, 0, 1]])
    if check == 1:
        tmp_lst = mul_martic(lst_point, [[ind, 0, 0], [0, 1, 0], [0, 0, 1]])
    elif check == 2:
        tmp_lst = mul_martic(lst_point, [[1, 0, 0], [0, ind, 0], [0, 0, 1]])
    else:
        print("Не то число")
        return lst_point

    return tmp_lst

def rotate_figure(angle):
    angle = radians(angle)

    return mul_martic(lst_point, [[cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0, 0, 1]])

def rotate_near_figure(angle, point):
    angle = radians(angle)

    res = mul_martic([[1, 0, point[0]], [0, 1, point[1]], [0, 0, 1]], [[cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0, 0, 1]])
    res = mul_martic(res, [[1, 0, -point[0]], [0, 1, -point[1]], [0, 0, 1]])
    res = mul_martic(lst_point, res)

    return res



def main():
    t.screen.setup(1200, 1000)
    t.screen.title("Welcome to the lab 2!")

    t.speed(0)
    t.hideturtle()

    draw_coord()

    while True:
        n = int(input("Что хотите увидеть? \n"))
        t.reset()
        if n == 0:
            draw_figure(lst_point)

        elif n == 1:
            c = int(input("На сколько сдвиг? \n"))
            draw_figure(shift_figure(1, c))

        elif n == 2:
            c = int(input("На сколько сдвиг? \n"))
            draw_figure(shift_figure(2, c))

        elif n == 3:
            draw_figure(mirror_figure(1))

        elif n == 4:
            draw_figure(mirror_figure(2))

        elif n == 5:
            draw_figure(mirror_line_figure())

        elif n == 6:
            c = float(input("Какой коэффициент? \n"))
            draw_figure(scale_figure(c))

        elif n == 7:
            c = float(input("Какой угол поворота? \n"))
            draw_figure(rotate_figure(c))

        elif n == 8: # fix
            c = float(input("Какой угол поворота? \n"))
            p = [float(i) for i in input("Какая точка? \n").split()]
            draw_figure(rotate_near_figure(c, p))

        else:
            break

    t.screen.exitonclick()
    t.screen.mainloop()





if __name__ == "__main__":
    main()






