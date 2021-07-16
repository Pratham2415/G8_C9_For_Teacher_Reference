import turtle

turtle.Screen().bgcolor('black')
turtle.speed(10)
n=1
colors=['red','green','blue','yellow','purple']

for angle in range(0,360,15):
    n=n+1
    if n==5:
        n=-1
    turtle.color(colors[n])
    turtle.seth(angle)
    turtle.circle(100)
