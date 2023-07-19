from turtle import Turtle


STARTING_POSITION = (0, -280)
STARTING_POSITION_DOWN = (0, 280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()

    def starting_position(self):
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.heading()

    def move_up(self):
        self.forward(MOVE_DISTANCE)
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)

    def move_down(self):
        self.forward(-MOVE_DISTANCE)
        if self.ycor() < -FINISH_LINE_Y:
            self.goto(STARTING_POSITION_DOWN)

