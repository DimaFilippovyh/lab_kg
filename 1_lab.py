from icecream import ic
import sys



def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0] * p2[1] - p2[0] * p1[1])
    return A, B, -C


def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        if D == Dx == Dy:
            return True
        else:
            return False


def two_lines(a, b, c, d):
    line_1 = line(a, b)
    line_2 = line(c, d)

    res = intersection(line_1, line_2)
    print('\n')
    if type(res) == tuple:
        print("Пересечение обнаружено: ", (res[0], res[1]))
    elif res:
        print("Прямые совпадают")
    else:
        print("Прямые параллельны")

#/////////////////////////////////////
def c_near_ab(a, b, c):
    if a[0] == c[0]:
        if c[1] > min(a[1], b[1]) and c[1] < max(a[1], b[1]):
            print("Точка лежит на луче")
        elif abs(c[1] - b[1]) < abs(c[1] - a[1]):
            print("Точка лежит на луче")
        else:
            print("Точка не лежит на луче")
    else:
        if c[0] > min(a[0], b[0]) and c[0] < max(a[0], b[0]):
            print("Точка лежит на луче")
        elif abs(c[0] - b[0]) < abs(c[0] - a[0]):
            print("Точка лежит на луче")
        else:
            print("Точка не лежит на луче")


def clockwise(a, b, c):
    line_1 = line(a, b)
    res = c[0]*line_1[0] + c[1]*line_1[1] + line_1[2]
    print('\n')
    if res == 0:
        print("Точка лежит на прямой")
    elif res > 0:
        print("Против часовой стрелки")
    elif res < 0:
        print("По часовой стрелке")


def two_surface(a, b, numb):
    res_1 = a[0]*numb[0] + a[1]*numb[1] + a[2]*numb[2] + a[3]
    res_2 = b[0]*numb[0] + b[1]*numb[1] + b[2]*numb[2] + b[3]
    if res_1 == 0 and res_2 == 0:
        print("Принадлежит")
    else:
        print("Не принадлежит")



def main():
    while True:
        i = int(input("Какая задача?"))
        if i == 1:
            print("1 task")
            print('Введите координаты концов первого отрезка.')
            a = int(input('Первая точка x = ')), int(input('y = '))
            b = int(input('Вторая точка x = ')), int(input('y = '))
            print('Введите координаты концов второго отрезка.')
            c = int(input('Первая точка x = ')), int(input('y = '))
            d = int(input('Вторая точка x = ')), int(input('y = '))

            two_lines(a, b, c, d)

        elif i == 2:
            print("2 task")
            a = int(input('Первая точка x = ')), int(input('y = '))
            b = int(input('Вторая точка x = ')), int(input('y = '))
            c = int(input('Наша точка x = ')), int(input('y = '))

            c_near_ab(a, b, c)

        elif i == 3:
            print("3 task")
            a = int(input('Первая точка x = ')), int(input('y = ')), int(input('z = '))
            b = int(input('Вторая точка x = ')), int(input('y = ')), int(input('z = '))
            c = int(input('Третья точка x = ')), int(input('y = ')), int(input('z = '))

            clockwise(a, b, c)

        elif i == 4:
            print("4 task")
            print('Введите коэффициенты прямых.')
            a = int(input('A_1 = ')), int(input('B_1 = ')), int(input('C_1 = ')), int(input('D_1 = '))
            b = int(input('A_2 = ')), int(input('B_2 = ')), int(input('C_2 = ')), int(input('D_2 = '))
            print('Введите координаты точки.')
            c = int(input('x = ')), int(input('y = ')), int(input('z = '))

            two_surface(a, b, c)

        elif i == 5:
            break

        else:
            sys.exit()



if __name__ == "__main__":
    main()

1 задача
two_lines((0, 0), (3, 3), (3, 0), (0, 3))
two_lines((0, 0), (3, 0), (3, 3), (0, 3))
two_lines((0, 0), (3, 0), (0, 3), (3, 1))
two_lines((0, 1), (2, 3), (2, 3), (0, 4))
two_lines((0, 0), (3, 3), (3, 3), (0, 0))
two_lines((0, 0), (3, 3), (0, 0), (3, 3))

c_near_ab((0, 0), (1, 1), (2, 2))
c_near_ab((1, 1), (0, 0), (2, 2))
c_near_ab((1, 1), (3, 3), (2, 2))
c_near_ab((3, 3), (1, 1), (2, 2))
c_near_ab((2, 2), (3, 3), (1, 1))

c_near_ab((1, 0), (1, 2), (1, 1))
c_near_ab((1, 0), (1, 2), (1, 3))
c_near_ab((1, 0), (1, 2), (1, -3))

clockwise((0, 0, 3), (3, 1, 0), (4, 4, 4)) # против часовой
clockwise((0, 0, 3), (4, 4, 4), (3, 1, 0)) # против часовой
clockwise((0, 0, 4), (4, 4, 4), (5, 5, 4)) # на прямой


two_surface((1, 2, 1, 54), (2, 9, -5, 32), (1, 2 ,3))
two_surface((1, 0, 0, 0), (0, 1, 0, 0), (1, 1, 0))










