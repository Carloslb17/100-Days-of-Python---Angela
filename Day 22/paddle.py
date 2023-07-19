from turtle import Turtle

INITIAL_COORDINATES = [350, 0]
PADDLE_SIZE = [20, 100]

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        #self.shapesize(stretch_wid=PADDLE_SIZE[0], strech_len=PADDLE_SIZE[1])
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()


    def initial_location_1(self):
        self.setposition(INITIAL_COORDINATES[0], INITIAL_COORDINATES[1])


    def initial_location_2(self):
        self.setposition(-INITIAL_COORDINATES[0], INITIAL_COORDINATES[1])

#We define the movement of the paddle
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)





