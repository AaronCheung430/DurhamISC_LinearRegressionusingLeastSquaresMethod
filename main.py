# Created by 2595161_qwwk95 from Durham University Interntaional Study Centre
# Last editied on 2021/05/27 18:00 GMT
# Copyright © 2021 2595161_qwwk95. All rights reserved.
# DUISC IFY Programming Techniques
# Summative 2 - Linear Regression using Least Squares Method

# Student No: 2595161
# DUID: qwwk95
# CLASS CODE: SFSCS_PT

# ------------------------------- Imported Packages -------------------------------
from util import config as cfg
from util import start as strt
from util import import_data, calculation
import numpy as np

# ---------------------------------- Main Program ---------------------------------

def main():

    end_program = False # variable used to check if user wants to exit program
    x_values, y_values, b_m, r_2 = np.array([]), np.array([]), np.array([]), 0 # set up variables

    # loop until end_program is True
    while not end_program:

        # call menu function and get user's option
        option = strt.menu()

        if option == 1: # import x, y values from csv
            read_file = True    # set variables
            file_path_error_message = ""
            import_file_message = "Importing your data via csv file"
            while read_file:    # loop when read_file is true
                cfg.clear_screen()
                print(f"You have chosen [{option}] {cfg.menu_options[option-1]}. \n")
                print("Please ensure your csv file is located in the 'data' folder. \nPress 'Enter' directly to use the default test data.")
                print(file_path_error_message)
                try:    # allow user to enter the file path
                    read_file_path = "data/" + input("Enter your file name (without .csv): \n") + ".csv"
                    if read_file_path == "data/.csv":   # check did user enter anything
                        read_file_path = cfg.default_read_file_path
                        import_file_message = "Importing default test data"
                    x_values, y_values = import_data.import_csv(read_file_path)  # call function to import csv file
                    cfg.clear_screen()
                    print(import_file_message, "\n")
                    cfg.time_animation(3, "CSV file imported successfully. \n")
                    cfg.countdown(4)
                    read_file = False
                except FileNotFoundError:   # handle the error if an exception occurs, to prevent the program from being terminating
                    file_path_error_message = "\nNO SUCH FILE! REMEMBER TO LOCATE YOUR CSV FILE IN THE 'DATA' FOLDER. \n"

        elif option == 2: # calcuate and display the linear regression line
            cfg.clear_screen()
            print(f"You have chosen [{option}] {cfg.menu_options[option-1]}. \n")
            if (x_values.size and y_values.size) == 0:    # check is variable array empty
                cfg.check_values()
                continue

            b_m, verify_b_m = calculation.find_linear_regress(x_values, y_values)   # call function to find the linear regression line
            print(f"The y-intercept is {b_m[0]} \nThe gradient is {b_m[1]}")
            print(f"The least squares regression line of this set of data is approximately Y = {b_m[1]:6.5e}x + {b_m[0]:6.5e} \n")
            print(f"Calculation using numpy - Verification \nThe y-intercept is {verify_b_m[0]} \nThe gradient is {verify_b_m[1]}")
            input("\nEnter to return to menu...") # pause the program

        elif option == 3: # calcuate and display the correlation coefficient
            cfg.clear_screen()
            print(f"You have chosen [{option}] {cfg.menu_options[option-1]}. \n")
            if (x_values.size and y_values.size) == 0:    # check are variables array empty
                cfg.check_values()
                continue
            elif b_m.size == 0:
                cfg.check_values(f"'[2] {cfg.menu_options[1]}' to find the equation", "equation")
                continue

            r_2, verify_r_2 = calculation.find_corr_coeff(x_values, y_values, b_m)  # call function to find the correlation coefficient
            print(f"The correlation coefficient of this set of data is approximately R\u00b2 = {r_2:6.5e} \n")
            print(f"Calculation using numpy - Verification \nThe correlation coefficient of this set of data is approximately R\u00b2 = {verify_r_2:6.5e}")
            input("\nEnter to return to menu...") # pause the program

        elif option == 4: # plot a scatter graph
            cfg.clear_screen()
            print(f"You have chosen [{option}] {cfg.menu_options[option-1]}. \n")
            if (x_values.size and y_values.size) == 0:    # check are variables empty
                cfg.check_values()
                continue
            elif b_m.size == 0:
                cfg.check_values(f"'[2] {cfg.menu_options[1]}' to find the equation", "equation")
                continue
            elif r_2 == 0:
                cfg.check_values(f"'[3] {cfg.menu_options[2]}' to find the correlation coefficient", "correlation coefficient")
                continue

            import_data.plot_graph(x_values, y_values, b_m, r_2)    # call function to plot the graph

        else: # option 5 - exit in controlled manner
            end_program = True  # set end_program Boolean to True

            # output messages to user
            print("Thank you for using this program")
            print("Quitting Program...")

        cfg.invalid_message = ""    # reset variable, to avoid invalid message to be shown in the next loop

        #### END OF MAIN PROGRAM


if __name__ == "__main__":
    main()
