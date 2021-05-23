# DUISC IFY Programming Techniques
# Summative 2 - Linear Regression using Least Squares Method

# Student No: 2595161
# DUID: qwwk95
# CLASS CODE: SFSCS_PT

# ------------------------------- Imported Packages -------------------------------
from util import config as cfg
from util import start as strt
# import numpy
# import pandas
# import matplotlib.pyplot as plt

# ---------------------------------- Main Program ---------------------------------

def main():

    end_program = False # variable used to check if user wants to exit program

    # loop until end_program is True
    while not end_program:

        # call menu function and get user's choice
        option = strt.menu()

        if option == 1: # import a x, y values from csv
            cfg.clear_screen()
            print(f"You have chosen [{option}] {cfg.menu_options[option-1]}. \n")
            # adjac_list = open_csv_file(cfg.read_file_path)
            # cfg.clear_screen()
            # cfg.time_animation(3, "CSV file imported successfully.")
            # cfg.countdown(4)
            print("option 1")

        elif option == 2: # calcuate and display the linear regression line
            cfg.clear_screen()
            print(f"You have chosen [{option}] {cfg.menu_options[option-1]}. \n")
            print("option 2")

        elif option == 3: # calcuate and display the correlation coefficient
            cfg.clear_screen()
            print(f"You have chosen [{option}] {cfg.menu_options[option-1]}. \n")
            print("option 3")

        elif option == 4: # plot scatter graph
            cfg.clear_screen()
            print(f"You have chosen [{option}] {cfg.menu_options[option-1]}. \n")
            print("option 4")

        else: # option 5 - exit in controlled manner

            end_program = True  # set end_program Boolean to True

            # output messages to user
            print("Thank you for using this program")
            print("Quitting Program...")

        #### END OF MAIN PROGRAM


if __name__ == "__main__":
    main()
