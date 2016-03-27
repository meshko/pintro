import turtle

def ksfl(n, len):
   global t, c
   if n == 0:
       t.color(c % 200, c % 200, c % 200)
       c+=10
       t.forward(len)
   else:
       fl = len/3.0
       ksfl(n-1, fl)
       t.right(60)
       ksfl(n-1, fl)
       t.left(120)
       ksfl(n-1, fl)
       t.right(60)
       ksfl(n-1, len - 2*fl)

def ksf(n, len):
   for i in range(0, 3):
      ksfl(n, len)
      t.left(120)
      

def htree(n, len):
    if n == 0: return
    t.forward(len)
    t.left(30)
    htree(n-1, len * .6)
    t.right(60)
    htree(n-1, len * .6)
    t.left(30)
    t.backward(len)


c = 0
t = turtle.Turtle()
t.screen.colormode(255)
t.speed(0)
t.penup()
t.backward(200)
t.right(90)
t.forward(100)
t.left(90)
t.pendown()
#for i in range (3, 6):
t.begin_fill()
ksf(2, 200)
t.end_fill()
t.left(180)
ksf(2, 200)
t.left(60)
ksf(2, 200)
#t.left(90)
#t.penup()
#t.backward(300)
#t.pendown()
#htree(10, 200)

turtle.exitonclick()
