import turtle

def sp(t, dir, angle):
	for i in range(0, 20):
		t.forward(2*i)
		if dir == "left":
			t.left(angle)	
		else:
			t.right(angle)

def st(t):
	t.begin_fill()
	for i in range(0, 6):
		t.forward(20)
		t.left(180-360/2/5)
	t.end_fill()

def circ(t):
	n = 100
	for i in range(0, n+1):
		t.forward(5)
		t.left(365.0 / n)

def gon(n):
   for i in range(0, n):
      t.forward(20)
      t.left(360.0/n)

def hello3(x, y):
   print t.pos()
   print x, y

t = turtle.Turtle()

#for i in range(1,4):
#	sp(t, "left", 90)
#	sp(t, "right", 90)

#st(t)
#circ(t)
#gon(45)
st(t)

turtle.onscreenclick(hello3, btn=1)
#turtle.exitonclick()
raw_input()
