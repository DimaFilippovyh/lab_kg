from turtle import *
import time



t = Turtle()
ch = Turtle()
m = Turtle()
s = Turtle()

t.hideturtle()



class Hands:
    
    def __init__(self, pensize, color, unit_angle, leng):
        self.pensize = pensize
        self.color = color
        self.unit_angle = unit_angle
        self.leng = leng



def draw_hand(turt, count, h_cls):
    turt.clear()
    turt.pensize(h_cls.pensize)
    turt.speed(0)
    turt.color(h_cls.color)
    turt.hideturtle()
    turt.up()
    turt.goto(0, 0)
    turt.down()
    turt.setheading(90)
    turt.rt(count * h_cls.unit_angle)
    turt.fd(h_cls.leng)



def main():
    t.screen.setup(920, 690)
    t.screen.title("clock")
    t.screen.bgpic("clock-without-hands.png")

    ch_cls = Hands(15, "red", 30, 100)
    m_cls = Hands(7, "green", 6, 200)
    s_cls = Hands(3, "blue", 6, 300)


    ch_ = int(input("Сколько часов? "))
    m_ = int(input("Сколько минут? "))
    s_ = 0

    draw_hand(ch, ch_, ch_cls)
    draw_hand(m, m_, m_cls)
    draw_hand(s, s_, s_cls)

    while True:
        if ch_ == 12:
            ch_ = 0

        if m_ == 60:
            ch_ += 1
            m_ = 0
            draw_hand(ch, ch_, ch_cls)

        if s_ == 60:
            s_ = 0
            m_ += 1
            draw_hand(m, m_, m_cls)

        draw_hand(s, s_, s_cls)
        s_ += 1
        time.sleep(0.85)


    t.screen.exitonclick()
    t.screen.mainloop()





if __name__ == "__main__":
    main()


















