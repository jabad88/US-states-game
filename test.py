import turtle
import pandas

screen = turtle.Screen()
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
states_list = data['state'].to_list()

guessed_states = []

user_guess = turtle.textinput("States Game","Guess a State: ").upper()

while len(guessed_states) < 50:
    if user_guess in states_list:
        guessed_states.append(user_guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        get_state_data = data[data.state == user_guess]
        print(int(get_state_data.x))



