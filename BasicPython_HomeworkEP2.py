import turtle
tao = turtle.Pen()
tao.shape('turtle')

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] #ประกาศค่าสี
turtle.bgcolor('black') #พื้นหลัง

'''Function วาดวงกลมโดยระบุสี'''
def Circle(a,b):
    for i in range(30):
            tao.pencolor(colors[a])
            tao.width(i//100 + 1)
            tao.circle(5*i)
            tao.pencolor(colors[b])
            tao.circle(-5*i)
            tao.right(i)

'''Function เคลียร์หน้าจอและกลับ Home'''
def Home():
    tao.clear()
    tao.penup()
    tao.home()
    tao.pendown()
    



Circle(2,4)
Home()


