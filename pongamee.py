import turtle

wnd = turtle.Screen()
wnd.title("pong by onuk")
wnd.bgcolor("black")
wnd.setup(width=800, height=600)
wnd.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Dispaly score Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Left Player : 0  Right Player: 0",
             align = "center", font = ("Courier", 24, "normal"))

# Score
score_a = 0
score_b = 0

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# keyboard binding
wnd.listen()
wnd.onkeypress(paddle_a_up, "w")
wnd.onkeypress(paddle_a_down, "s")
wnd.onkeypress(paddle_b_up, "Up")
wnd.onkeypress(paddle_b_down, "Down")


# main game loop
while True:
    wnd.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # Top screen
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  #Bouncing the ball

    # Bottom screen
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  #Bouncing the ball

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1  #Bouncing the ball
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1  #Bouncing the ball
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and Ball collisions
    if (ball.xcor() > 340) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
    # Paddle limit
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)

    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)



