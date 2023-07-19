from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Wich turtle will win the race? Enter a color ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

position_x = -230
position_y = -100

for color in colours:
    colors[turtle_index] = Turtle(shape="turtle")
    colors[turtle_index].penup()
    colors[turtle_index].goto(x=position_x, y=position_y)
    position_y += 36

red.colour("red")




screen.exitonclick()









