
    
import turtle
   
t= turtle.Pen()
turtle.bgcolor('grey')
t.speed(2)
 
#Code for A only   
t.width(15)
t.pencolor('cyan')
t.left(60)
t.forward(125)
t.right(120)
t.forward(125)
t.goto(100,45)
t.right(120)
t.forward(70)
t.penup()



#Code for D only

t.goto(155,0)
t.pendown()
t.pencolor('yellow')
t.right(90)
t.forward(112)
t.goto(155,0)
t.right(90)
t.circle(60,180)
t.penup()

# Code for I only

t.goto(255,0)
t.pendown()
t.pencolor('red')
t.right(90)
t.forward(112)
t.penup()
t.goto(220,112)
t.pendown()
t.right(90)
t.forward(70)
t.penup()
t.goto(220,0)
t.right(0)
t.pendown()
t.forward(70)

# Code for T only

t.penup()
t.goto(360,0)
t.right(-90)
t.pencolor('cyan')
t.pendown()
t.forward(112)
t.penup()
t.goto(325,112)
t.right(90)
t.pendown()
t.forward(70)

# Code for Y only

t.penup()
t.goto(460,0)
t.pendown()
t.pencolor('yellow')
t.right(-90)
t.forward(52)
t.left(30)
t.forward(70)
t.goto(460,52)
t.right(60)
t.forward(70)

#Code for last A only
t.penup()
t.goto(515,0)
t.pencolor('cyan')
t.pendown()
t.right(0)
t.forward(125)
t.right(120)
t.forward(125)
t.goto(615,45)
t.right(120)
t.forward(70)

# Code for the Borders

t.penup()
t.goto(-30,-25)
t.pendown()
t.width(5)
t.pencolor('white')
t.right(180)
t.forward(680)
t.pencolor('orange')
t.circle(90,180)
t.pencolor('white')
t.forward(680)
t.pencolor('orange')
t.circle(90,180)
t.penup()

# only for Design
t.speed(7)
col=('yellow','cyan','red')
t.goto(-250,20)
t.pendown()

for i in range(45):
    t.color(col[i%3])
    t.forward(100)
    t.left(123)
    
    








    
    