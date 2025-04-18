import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Catch Game")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()

# Create the target turtle
target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()
target.goto(random.randint(-250, 250), random.randint(-250, 250))

# Movement functions
def move_up():
    y = player.ycor()
    player.sety(y + 20)

def move_down():
    y = player.ycor()
    player.sety(y - 20)

def move_left():
    x = player.xcor()
    player.setx(x - 20)

def move_right():
    x = player.xcor()
    player.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Game loop
while True:
    # Check if player touched the target
    if player.distance(target) < 20:
        target.goto(random.randint(-250, 250), random.randint(-250, 250))
        print("You caught the target!")

screen.mainloop()
