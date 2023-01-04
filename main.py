import turtle
import pandas

DATA = pandas.read_csv("50_states.csv")
FONT = ("Arial", 10, "normal")
LIST_OF_ANSWERS = []
SCORE = 0
GAME_ON = True
STATES_TO_LEARN = []

us_map = turtle.Screen()
us_map.title("Guess The State Game")
image = "blank_states_img.gif"
us_map.addshape(image)
turtle.shape(image)
text = turtle.Turtle()
text.hideturtle()
text.color("black")
text.penup()
states_list = DATA.state.to_list()


while GAME_ON and len(LIST_OF_ANSWERS) < 50:
    answer = us_map.textinput(title=f"{SCORE}/50 correct answers", prompt="Insert state's name here:").title()
    if answer in states_list:
        LIST_OF_ANSWERS.append(answer)
        data_state = DATA[DATA.state == answer]
        text.goto(int(data_state.x), int(data_state.y))
        text.write(f"{answer}", font=FONT)
        SCORE += 1
    elif answer == "Check" or answer == "check":
        STATES_TO_LEARN = [state for state in states_list if state not in LIST_OF_ANSWERS]
        for item in STATES_TO_LEARN:
            missing_state = DATA[DATA.state == item]
            text.goto(int(missing_state.x), int(missing_state.y))
            text.write(f"{item}", font=FONT)
    elif answer == "Exit" or answer == "exit":
        break


































































