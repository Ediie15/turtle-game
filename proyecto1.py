import turtle
import random

s = turtle.Screen()
s.title("Juego de Tortugas")
s.bgcolor('#07E4F2') #Codigo Hexadecimal para color

jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()

jugador1.hideturtle()
jugador1.shape("turtle") 
jugador1.color("green", "green")
jugador1.shapesize(2,2,2)
jugador1.pensize(3)

jugador2.hideturtle()
jugador2.shape("turtle")
jugador2.color("blue", "blue")
jugador2.shapesize(2,2,2)
jugador2.pensize(3)

jugador1.penup()
jugador1.goto(200,200)
jugador1.pendown()
jugador1.circle(40)

jugador1.penup()
jugador1.goto(-250,225)
jugador1.showturtle()

jugador2.penup()
jugador2.goto(200,-200)
jugador2.pendown()
jugador2.circle(40)

jugador2.penup()
jugador2.goto(-250,-170)
jugador2.showturtle()


dado = [1,2,3,4,5,6]

for i in range(20):
    if jugador1.pos() >= (200,200):
        print("La tortuga verde es la ganadadora")
        break
    elif jugador2.pos() >= (200,-200):
        print("La tortuga azul es la ganadora")
        break
    else:
        turno1 = input("Pulsa ENTER para avanzar la tortuga verde")
        turno1 = random.choice(dado)
        print("Tu número es: ",turno1, "\nAvanzas: ", turno1*20)
        jugador1.pendown()
        jugador1.forward(20*turno1)

        turno2 = input("Pulsa ENTER para avanzar la tortuga azul")
        turno2 = random.choice(dado)
        print("Tu número es: ",turno1, "\nAvanzas: ", turno2*20)
        jugador2.pendown()
        jugador2.forward(20*turno2)

turtle.done()