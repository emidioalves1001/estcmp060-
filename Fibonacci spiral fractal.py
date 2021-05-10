# -- coding: utf-8 --
import turtle
import math
def fiboPlot(n):
    a=0
    b=1
    aq=a
    bq=b
    x.pencolor("blue")
    x.forward(b*fator)
    x.left(90)
    x.forward(b*fator)
    x.left(90)
    x.forward(b*fator)
    x.left(90)
    x.forward(b*fator)
    t=bq
    bq=bq+aq
    aq=t
    for i in range(1,n):
        x.backward(aq*fator)
        x.right(90)
        x.forward(bq*fator)
        x.left(90)
        x.forward(bq*fator)
        x.left(90)
        x.forward(bq*fator)
        t=bq
        bq=bq+aq
        aq=t
    x.penup()
    x.setposition(fator,0)
    x.seth(0)
    x.pendown()
    x.pencolor("red")
    x.left(90)
    for i in range(n):
        print(b)
        fdwd=math.pi*b*fator/2
        fdwd/=90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        t=a
        a=b
        b=t+b
fator=1
n=int(input("Digite o número de iterações (tem que ser > 1): "))
if(n>0):
    print("Sequência de Fibonacci com", n, "elementos :")
    x=turtle.Turtle()
    x.speed(100)
    fiboPlot(n)
    turtle.done()
else:
    print("Número de iterações tem que ser > 0")