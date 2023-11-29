import turtle as t
from math import sqrt

phi = (1+sqrt(5)) / 2
const = 500
base = phi * const
altura = const

t.title('Golden Spiral')
t.speed(5)
t.color('black', 'white')
t.width(3)
t.penup()
t.setpos((phi*-const)/2, -const/2)
t.pendown()

for i in range(2):
    t.forward(base)
    t.left(90)
    t.forward(altura)
    t.left(90)

t.forward(altura)
t.left(90)

novoLado = altura
for j in range(10):
    t.forward(novoLado)
    t.backward(((base-altura)**(j+1))/const**j)
    t.right(90)
    novoLado = ((base-altura)**(j+1))/const**j

t.penup()
t.setpos((phi*-const)/2, -const/2)
t.pendown()
t.setheading(90)

arco_90 = altura
for k in range(10):
    t.circle(arco_90, 90)
    arco_90 = ((base-altura)**(k+1))/const**k

t.hideturtle()
t.mainloop()