import os
import turtle
import pandas
from os.path import exists
from names import Name

states = Name()
screen = turtle.Screen()

#   Setting USA map image
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape("blank_states_img.gif")
turtle.shape(image)

#   Empty Dict and List to further contents
saved_states = {}
states_mentioned = []


save_exist = exists('save.csv')
states_pos = states.states_pos
states.creating_dict()

#   Saves the game
def saving():
    saved_states["states"] = states_mentioned
    save = pandas.DataFrame(saved_states)
    save.to_csv('save.csv')


#   Checking exists a save to load

if save_exist:
    save_load = pandas.read_csv("save.csv")
    for said_states in save_load["states"]:
        states.name_moving(said_states)
        states.name_removing(said_states)
        states_mentioned.append(said_states)
        saved_states["states"] = states_mentioned
else:
    pass
game_on = True
while game_on:
    question = screen.textinput(title=f'{len(states_mentioned)}/50 States Correct', prompt="What's another state's name?").title()
#   Clear all the data and restart the game
    if question == "Clear":
        if save_exist is True:
            os.remove('save.csv')
            save_exist = False
            screen.reset()
            states_mentioned = []
            states.creating_dict()
#   Save and exit the game
    elif question == "Exit":
        screen.bye()
        saving()
        game_on = False
    elif question not in states_pos:
        pass
#   Call the methods to move the name, exclude the already wrote data and save
    elif question in states_pos:
        states.name_moving(question)
        states.name_removing(question)
        states_mentioned.append(question)
        saving()
        save_exist = True
#   Finished game screen
    if states_pos == {}:
        states.congrats()
        screen.exitonclick()
        game_on = False


