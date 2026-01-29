import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
turtle.goto(0,0)
t_write = turtle.Turtle()
t_write.penup()
t_write.hideturtle()

score = 0

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

correct_guesses = []

def correct_guess():
    if answer_state.title() in correct_guesses:
        return False
    elif answer_state.title() in [state.title() for state in state_list]:
        return True
    else:
        return False

game_on = True
while game_on:
    answer_state = screen.textinput(title=f"{score}/50 Correct", prompt="What's another state's name?")
    if answer_state == "Exit":
        missing_list = []
        for state in state_list:
            if state not in correct_guesses:
                missing_list.append(state)
        new_data = pandas.DataFrame(missing_list)
        new_data.to_csv("states_to_learn.csv")

        break
    if correct_guess():
        state_row = data[data.state == answer_state.title()]
        x_coor = state_row.x.iloc[0]
        y_coor = state_row.y.iloc[0]
        t_write.goto(x_coor,y_coor)
        t_write.write(answer_state.title())
        correct_guesses.append(answer_state.title())
        score +=1
        if score == 50:
            screen.textinput(title="Congratulation", prompt = "You have completed the quiz")
            game_on = False
