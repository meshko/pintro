import turtle

def ksfl(t1, n, len):
   for t in turtles:
      if n == 0:
         t.forward(len)
      else:
         fl = len/3.0
         ksfl(t, n-1, fl)
         t.right(60)
         ksfl(t, n-1, fl)
         t.left(120)
         ksfl(t, n-1, fl)
         t.right(60)
         ksfl(t, n-1, len - 2*fl)

def ksf(n, len):
  for i in range(0, 3):
     for t in turtles:
         ksfl(t, n, len)
         t.left(120)

def make_turtle(x, y):
   t = turtle.Turtle()
   t.screen.colormode(255)
   t.speed(0)
   t.penup()
   t.backward(x)
   t.right(90)
   t.forward(y)
   t.left(90)
   t.pendown()
   return t
      
turtles = [make_turtle(200, 100), make_turtle(-200, -100)]
c = 0
ksf(2, 200)

turtle.exitonclick()
