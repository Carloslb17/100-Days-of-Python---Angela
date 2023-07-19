import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
AXIS_X = 300
AXIS_Y = 280
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []


    def create_cars(self):
        random_chance = random.randint(1, 10)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            list_value = random.randint(0, len(COLORS) - 1)
            new_car.color(COLORS[list_value])
            new_car.penup()
            random_start_y = random.randint(-AXIS_Y, AXIS_Y)
            new_car.goto(300, random_start_y)
            new_car.showturtle()
            self.all_cars.append(new_car)

    def move_forward(self):
        for car in self.all_cars:
            if car.xcor() != -300:
                car.forward(-STARTING_MOVE_DISTANCE)
            else:
                car.hideturtle()


