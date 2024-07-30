import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Stick Man Crossing the Street")
screen.bgcolor("lightblue")

# Create a turtle for the stick man
stick_man = turtle.Turtle()
stick_man.hideturtle()
stick_man.speed(0)
stick_man.pensize(3)

# Draw the stick man
def draw_stick_man(x, y):
    stick_man.penup()
    stick_man.goto(x, y)
    stick_man.pendown()
    stick_man.circle(10)  # Head
    stick_man.right(90)
    stick_man.forward(30)  # Body
    stick_man.right(45)
    stick_man.forward(20)  # Right leg
    stick_man.backward(20)
    stick_man.left(90)
    stick_man.forward(20)  # Left leg
    stick_man.backward(20)
    stick_man.right(45)
    stick_man.forward(20)  # Body continuation
    stick_man.right(45)
    stick_man.forward(20)  # Right arm
    stick_man.backward(20)
    stick_man.left(90)
    stick_man.forward(20)  # Left arm
    stick_man.backward(20)
    stick_man.right(45)
    stick_man.penup()

# Animate the stick man crossing the street
def move_stick_man():
    stick_man.clear()
    x = -200
    y = 0
    while x < 200:
        draw_stick_man(x, y)
        x += 10
        screen.update()
        stick_man.clear()
        turtle.time.sleep(0.1)

# Set up screen for animation
screen.tracer(0)
move_stick_man()

# Keep the window open until clicked
screen.exitonclick()
