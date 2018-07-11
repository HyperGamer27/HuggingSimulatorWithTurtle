
# NOTE: Hugging simulator coded using 'Python With Turtle'.

# NOTE: use 'clear' instead of 'cls' if you are using Linux or Mac OS

import turtle, time, math, random, os, sys

screenX = 1366
screenY = 768

t, papa, s = turtle.Turtle(), turtle.Turtle(), turtle.Screen()

papa.speed(0.5)

gameOver = False

speed, score = 2, 0

random.seed(time.time())

def moveUp():
    t.setheading(90)

def moveDown():
    t.setheading(-90)

def moveLeft():
    t.setheading(180)
    t.shape('trex.gif')

def moveRight():
    t.setheading(0)
    t.shape('trexflip.gif')

def game_over():
    s.reset()
    s.title('Game Over!')
    turtle.penup()
    turtle.write('Game Over! Final score: ' + str(score), move=False, align="center", font=("Arial", 32, "normal"))
    turtle.goto(0, -40)
    turtle.write('Click on the screen to exit. Code returned 0', move = False, align = 'center', font=('Arial', 12, 'normal'))
    t.hideturtle()
    papa.hideturtle()
    turtle.hideturtle()
    s.exitonclick()
    os.system('cls')

s.onkey(moveUp, 'w')
s.onkey(moveDown, 's')
s.onkey(moveLeft, 'a')
s.onkey(moveRight, 'd')

s.onkey(game_over, 'x')

s.listen()

t.penup()
papa.penup()

s.addshape('bird.gif')
s.addshape('turtle.gif')
s.addshape('trex.gif')
s.addshape('trexflip.gif')
s.addshape('rabbit.gif')
s.addshape('ghost.gif')
s.addshape('invader.gif')

shapes = ['rabbit.gif', 'turtle.gif', 'bird.gif', 'ghost.gif', 'invader.gif']

t.shape('trexflip.gif')

papa.shape('bird.gif')

papa.setposition(-200, -200)

s.setup(screenX, screenY)

while not gameOver:

    s.title("Hugging simulator Score: " + str(score))

    if math.sqrt((papa.position()[0] - t.position()[0]) ** 2 + (papa.position()[1] - t.position()[1]) ** 2) < 50:
        score += 1
        papa.setposition(random.randint(int(-screenX / 4), int(screenX / 4)), random.randint(int(-screenY / 4), int(screenY / 4)))
        papa.shape(shapes[random.randint(0, 4)])

    if abs(t.position()[0]) > screenX / 2 or abs(t.position()[1]) > screenY / 2:
        gameOver = True
        game_over()
        s.exitonclick()

    t.forward(2 * speed)

    '''

    if score > 5:
        speed = 1
        t.forward(speed)
    if score > 10:
        speed = 2
        t.forward(speed)
    if score > 15:
        speed = 3
        t.forward(speed)
    if score > 20:
        speed = 4
        t.forward(speed)
    '''
 
