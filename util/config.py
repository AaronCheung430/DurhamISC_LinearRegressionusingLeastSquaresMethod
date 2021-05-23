# config.py
# initialise most variable I needed in the project

import os
from time import sleep
import pandas as pd
import numpy as np

# set up the lists for the menu options
menu_options = ["Import a list of x and y values from a csv file", "Calculate the linear regression line", "Calculate the correlation coefficient", "Plot a scatter graph", "Quit the Program"]

# declare variables
valueError_message = "Oops! That was a text. Please try again with a valid number... \n"
welcome_message = "Welcome to the Linear Regression using Least Squares Method. \nPlease type the number below."
invalid_message = ""

default_read_file_path = "data/test_data.csv" # file path for file to be read

# to check which operation system is the user running this program on and clear the screen in the cell prompt
def clear_screen():

    # to check is the user using linux or mac. The os.name for lunux and mac is "posix".
    if os.name == "posix":
        _ = os.system("clear")
    else:
        # for other operation system, e.g. window.
        _ = os.system("cls")

# to preform the time delay animation
def time_animation(t, message="Done!      "):
    for i in range(t):
        for frame in r'-\|/-\|/':
            # Back up one character then print our next frame in the animation
            print('\rloading ', frame, sep='', end='', flush=True)
            sleep(0.125)

    print("\r" + message)

# to countdown, get parameters about how many seconds is the countdown going to run, and the message that will show.
def countdown(s, message = "Returning to main menu in"):

    # print countdown on the same line, until s is 0
    while s:
        timer = "{:01d}".format(s)
        print(message, timer, end="\r")
        sleep(1)
        s -= 1