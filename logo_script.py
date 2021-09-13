import turtle
t = turtle.Turtle()

def inicial():
	t.speed(5)
	t.left(-90)
	t.forward(100)
	t.left(120)
	t.forward(50)
	t.left(120)
	t.forward(50)
	t.left(-120)
	t.forward(50)
	t.left(120)
	t.forward(50)

def iteracion(num):
  for i in range(num):
    if i%2 == 0:
    	inicial()
    else:
      t.begin_fill()
      inicial()
      t.end_fill()
      
    
#inicial()  

iteracion(4)
