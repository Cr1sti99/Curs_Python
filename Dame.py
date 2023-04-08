# Problema damelor. Actiuni: genereaza cate o noua serie de 8 dame, pana cand nu mai sunt doua pe diagonala
# pozitia damelor este generata aleator, cate o dama, pe fiecare linie
import turtle
import random
import time

screen = turtle.Screen()
screen.title("Dame")
screen.bgcolor("Green")
screen.setup(width=540, height=540)
screen.tracer(1, 0.7)

colors = ["blue", "white"]
square_size = 60
num_rows = 8
num_cols = 8

# Desenează pătratele
for i in range(num_rows):
    for j in range(num_cols):
        square = turtle.Turtle()
        square.shape("square")
        square.color(colors[(i+j) % 2])
        square.shapesize(stretch_wid=2, stretch_len=2)
        square.penup()
        square.goto((-num_cols/2 + j) * square_size, (num_rows/2 - i) * square_size)

diagonal_ok = False

circles = []

while not diagonal_ok:
    # Șterge damele vechi de pe ecran
    for t in circles:
        t.hideturtle()
    circles = []

    used_rows = []
    used_cols = []

    for j in range(num_cols):
        while True:
            row = random.randint(0, num_rows - 1)
            if row not in used_rows and j not in used_cols:
                used_rows.append(row)
                used_cols.append(j)
                break
        circle = turtle.Turtle()
        circle.shape("circle")
        circle.color("black")
        circle.shapesize(30/20)
        circle.penup()
        circle.goto((-num_cols/2 + j) * square_size, (num_rows/2 - row) * square_size)
        circles.append(circle)

    diagonal_ok = True
    for i in range(num_cols - 1):
        for j in range(i + 1, num_cols):
            if abs(used_cols[i] - used_cols[j]) == abs(used_rows[i] - used_rows[j]):
                diagonal_ok = False
                break
        if not diagonal_ok:
            break

    if diagonal_ok:
        print("Tablou dame generat cu succes")
    else:
        time.sleep(0.1)

    screen.tracer(0)
    for t in circles:
        t.showturtle()
    screen.tracer(1)
