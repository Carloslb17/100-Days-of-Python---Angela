from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


turtle = Turtle()
screen = Screen()
paddle_one = Paddle()
paddle_second = Paddle()
ball = Ball()
scoreboard = Scoreboard()


#Screen Set up
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


#Movements of the paddle
paddle_one.initial_location_1()
paddle_second.initial_location_2()

screen.listen()

#Paddle's movemements
screen.onkey(paddle_one.move_up, "Up")
screen.onkey(paddle_one.move_down, "Down")
screen.onkey(paddle_second.move_up, "w")
screen.onkey(paddle_second.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detection of collisions
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_one) < 50 and ball.xcor() > 320 or ball.distance(paddle_second) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddl misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


    # Detect R paddl misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()




