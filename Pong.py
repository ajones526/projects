import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=600, height=400)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=1, stretch_len=5)
paddle_a.penup()
paddle_a.goto(-250, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=1, stretch_len=5)
paddle_b.penup()
paddle_b.goto(250, 0)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Paddle movement functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 190:
        y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -190:
        y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 190:
        y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -190:
        y -= 20
    paddle_b.sety(y)

# Keyboard bindings
screen.listen()
screen.onkey(paddle_a_up, "w")
screen.onkey(paddle_a_down, "s")
screen.onkey(paddle_b_up, "Up")
screen.onkey(paddle_b_down, "Down")

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1

    # Paddle and ball collisions
    if (ball.xcor() > 240 and ball.xcor() < 250) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.color("blue")
        ball.setx(240)
        ball.dx *= -1

    elif (ball.xcor() < -240 and ball.xcor() > -250) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.color("red")
        ball.setx(-240)
        ball.dx *= -1
