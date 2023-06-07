import turtle
import pandas


screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
print(states_list)

number_correct = 0
guessed_states = []
missed_states = []

while len(guessed_states) < 50:
    answer_state = turtle.textinput(f"{number_correct}/50 States Correct", "What's another state name?").title()

    if answer_state in states_list:
        add_to_guessed_states = guessed_states.append(answer_state)
        number_correct += 1
        state_data = (data[data.state == answer_state])
        state_data_x = int(state_data.x)
        state_data_y = int(state_data.y)

        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(state_data_x, state_data_y)
        t.write(answer_state.title())

    if answer_state == "Exit":
        missed_states = [x for x in states_list if x not in guessed_states]
        # for x in states_list:
        #     if x not in guessed_states:
        #         missed_states.append(x)
        print(missed_states)
        # study_dictionary = {
        #     "Study These": missed_states,
        # }

        # df = pandas.DataFrame(study_dictionary)
        # df.to_csv("states_to_learn.csv")
        break