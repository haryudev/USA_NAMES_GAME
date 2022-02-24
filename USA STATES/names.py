import pandas
from turtle import Turtle


class Name(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        #   Create lists with the positions values and names of the states
        self.states_data = pandas.read_csv("50_states.csv")
        self.states_x_pos = self.states_data['x'].to_list()
        self.states_y_pos = self.states_data['y'].to_list()
        self.states_names = self.states_data['state'].to_list()
        self.states_pos = {}

    #   Creates a dictionary with the states names and their positions
    def creating_dict(self):
        self.hideturtle()
        self.penup()
        position = 0
        for state_name in self.states_names:
            self.states_pos[state_name] = (self.states_x_pos[position], self.states_y_pos[position])
            position += 1

    #   Moves the name to his position on the map
    def name_moving(self, name):
        self.goto(self.states_pos[name])
        self.write(f"{name}")

    #   Remove the already inputted name from the dict
    def name_removing(self, name):
        self.states_pos.pop(name)

    #   Gives congratulations to the person that ended the game
    def congrats(self):
        self.hideturtle()
        self.goto(-170, 250)
        self.write(arg="Congratulations!!! You know all the states of U.S!!", font=("Times New Roman", 15, 'normal'))
