from turtle import *
from colorsys import *

pen = Turtle()

def turtleflower(velocidad):
    bgcolor("black")
    speed(velocidad)
    h = 0 
    for i in range(371):
        c = hsv_to_rgb(h, 1, 1)
        h += 0.005
        color(c)
        circle(-i*0.68, 200)
        right(80)

    done()

def turtlecopo(velocidad):
    bgcolor("black")
    speed(velocidad)
    h = 0 
    for i in range(371):
        c = hsv_to_rgb(h, 1, 1)
        h += 0.005
        color(c)
        circle(-i*0.68, 200)
        right(100)

    done()

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart(vel):
    bgcolor("black")
    pen.speed(vel)
    pen.color("red")
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
  

def txt():
    pen.up()
    pen.setpos(-68, 95)
    pen.down()
    pen.color('lightgreen')
    pen.write("GeeksForGeeks", font=(
      "Verdana", 12, "bold"))
  

def q_velocidad():
    segundos = int(input("a cuanta velocidad quieres hacerlo?"))
    velocidad= 1/segundos
    return velocidad

def funcion():
    funcion_elegida= input("elige entre un copo, un corazon o una flor: ")
    if funcion_elegida=="copo":
        return 1
    elif funcion_elegida=="corazon":
        return 2
    elif funcion_elegida=="flor":
        return 3
    else:
        return 0

def main():
    v=q_velocidad()
    make_f = funcion()
    if make_f==1:
        turtlecopo(v)
    if make_f==2:
        heart(v)
    if make_f==3:
        turtleflower(v)
    else:
        print("error, intentalo de nuevo")
    

if __name__ == "__main__":
    main()