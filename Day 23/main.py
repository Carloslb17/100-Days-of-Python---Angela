from player import Player
from turtle import Turtle, Screen
from car_manager import CarManager
import time

screen = Screen()
player = Player()
car = CarManager()

screen.setup(width=600, height=600)
screen.tracer(0)

player.starting_position()

#How to move the turtle
screen.listen()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_forward()




screen.exitonclick()