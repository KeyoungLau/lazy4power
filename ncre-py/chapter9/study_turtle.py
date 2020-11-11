import turtle as t
t.speed(1)
t.pensize(3)
t.penup()
t.goto(-200,-50)
t.pendown()
t.pencolor('purple')
t.begin_fill()
t.color('red')
t.circle(40,steps=3)
t.end_fill()

# 四边形
t.penup()
t.goto(-100,-50)
t.pendown()
t.begin_fill()
t.color('blue')
t.circle(40, steps=4)
t.end_fill()


# 五边形
t.penup()
t.goto(0,-50)
t.pendown()
t.begin_fill()
t.color('green')
t.circle(40, steps=5)
t.end_fill()

# 六边形
t.penup()
t.goto(100,-50)
t.pendown()
t.begin_fill()
t.color('yellow')
t.circle(40, steps=6)
t.end_fill()

# 圆形
t.penup()
t.goto(200,-50)
t.pendown()
t.begin_fill()
t.color('purple')
t.circle(40)
t.end_fill()

# 写文字
t.color('Green')
t.penup()
t.goto(-100,50)
t.pendown()
t.write("Cool Colorful Shapes", font=('Times', 18, 'bold'))
t.hideturtle()
t.done()