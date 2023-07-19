import pandas as pd
import turtle
from turtle import Turtle

screen = turtle.Screen()
text = Turtle()
text.hideturtle()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0

states_df = pd.read_csv("50_states.csv")

print(states_df)

game_is_on = True

answers = []
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")

    row_bool = states_df[states_df["state"] == answer_state].any()

    #missing_states = [state for state in all_states if state not in guessed_states]
    if row_bool['state'] == True:
        correct_answer = states_df[states_df["state"] == answer_state]
        x_cor = correct_answer['x']
        y_cor = correct_answer['y']
        text.color('black')
        style = ('Courier', 8)
        text.penup()
        text.goto(int(x_cor), int(y_cor))
        text.write(answer_state, font=style, align='center')
        answers.append(text)
        score += 1
    #if pd.:
        #score += 1
   # else:
        #score += 1


screen.exitonclick()